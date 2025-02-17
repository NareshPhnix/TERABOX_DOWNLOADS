import os
import re
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message, CallbackQuery
import logging
import asyncio
from datetime import datetime
from pyrogram.enums import ChatMemberStatus
from dotenv import load_dotenv
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated
from config import TELEGRAM_API, TELEGRAM_HASH, BOT_TOKEN, DUMP_CHAT_ID, ADMINS, HELP_TXT, FSUB_ID, WAIT_MSG, REPLY_ERROR, FORCE_MSG, DB_URI, DB_NAME, BOT_USERNAME, KEYWORDS
from os import environ
import time
from helper import subscribed, change_domain, format_duration, get_video_duration, update_url_if_keyword_exists
from database import add_user, del_user, full_userbase, present_user
from status import format_progress_bar
from video import download_video, upload_video
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1002212612017
pyrogram.utils.MIN_CHANNEL_ID = -1002220732120
pyrogram.utils.CHANNEL_ID = -1002212612017
pyrogram.utils.MIN_CHANNEL_ID = -1002232462602
pyrogram.utils.CHANNEL_ID = -1002232462602

load_dotenv('sconfig.env', override=True)
logging.basicConfig(level=logging.INFO)

api_id = os.environ.get('TELEGRAM_API', '28192191')
if len(api_id) == 0:
    logging.error("TELEGRAM_API variable is missing! Exiting now")
    exit(1)

id_pattern = re.compile(r'^.\d+$')

ADMINS = "2048030675"

api_hash = os.environ.get('TELEGRAM_HASH', '663164abd732848a90e76e25cb9cf54a')
if len(api_hash) == 0:
    logging.error("TELEGRAM_HASH variable is missing! Exiting now")
    exit(1)
    
bot_token = os.environ.get('BOT_TOKEN', '7458046887:AAHJ0_DHcI5-4CfwcyfCsVsTYecRE2EhPRI')
if len(bot_token) == 0:
    logging.error("BOT_TOKEN variable is missing! Exiting now")
    exit(1)


dump_id = os.environ.get('DUMP_CHAT_ID', '-1002212612017')
if len(dump_id) == 0:
    logging.error("DUMP_CHAT_ID variable is missing! Exiting now")
    exit(1)
else:
    dump_id = int(dump_id)

fsub_id = os.environ.get('FSUB_ID', '-1002232462602')
if len(fsub_id) == 0:
    logging.error("FSUB_ID variable is missing! Exiting now")
    exit(1)
else:
    fsub_id = int(fsub_id)

log_id = os.environ.get('LOG_ID', '-1002220732120')
if len(log_id) == 0:
    logging.error("LOG_ID variable is missing! Exiting now")
    exit(1)
else:
    log_id = int(log_id)

DB_URI = os.environ.get('DB_URI', 'mongodb+srv://phoenix:Mongo.12345nht@cluster123.1mvajso.mongodb.net/?retryWrites=true&w=majority&appName=cluster123')
if len(DB_URI) == 0:
    logging.error("DB_URI variable is missing! Exiting now")
    exit(1)

keywords = os.getenv("KEYWORDS").split(',')


app = Client("my_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)



#==============================================================================================================================================================#


@app.on_message(filters.command('start') & filters.private & subscribed)
async def not_joined(client: Client, message: Message):
    id = message.from_user.id
    uname = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    log_message =f"{id} / {uname} / {first_name} started the bot"
    log_message1 = f"""#ɴᴇᴡ_ᴜꜱᴇʀ
◉ ᴜꜱᴇʀ-ɪᴅ: <code>{id}</code>
◉ ᴀᴄᴄ-ɴᴀᴍᴇ: {first_name} {last_name}
◉ ᴜꜱᴇʀɴᴀᴍᴇ: @{uname}
after joining
"""
    if not await present_user(id):
        try:
            await add_user(id)
            await app.send_message(log_id, log_message1)
            await client.send_message(log_id, log_message1)
        except:
            pass
    sticker_message = await message.reply_sticker("CAACAgIAAxkBAAEYonplzwrczhVu3I6HqPBzro3L2JU6YAACvAUAAj-VzAoTSKpoG9FPRjQE")
    await asyncio.sleep(2)
    await sticker_message.delete()
    user_mention = message.from_user.mention
    reply_message = f"<b>ᴡᴇʟᴄᴏᴍᴇ, {user_mention}</b>.\n\n<b>😎ɪ ᴀᴍ ᴀ ᴛᴇʀᴀʙᴏx ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ🤖.\n \nsᴇɴᴅ ᴍᴇ ᴀɴʏ ᴛᴇʀᴀʙᴏx ʟɪɴᴋ🔗 ɪ ᴡɪʟʟ ᴅᴏᴡɴʟᴏᴀᴅ📥 ɪᴛ ᴡɪᴛʜɪɴ ғᴇᴡ sᴇᴄᴏɴᴅs🚀</b>."
    #join_button = InlineKeyboardButton("ᴊᴏɪɴ😎 ", url="https://t.me/teraboxxdownloader")
    #developer_button = InlineKeyboardButton("ᴅᴇᴠᴇʟᴏᴘᴇʀ⚡️", url="https://t.me/Scorpsnights")


   
    
    buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="Aʙᴏᴜᴛ📃", callback_data="about"),
            InlineKeyboardButton(text="Hᴇʟᴘ🔍", callback_data="help")
        ],
        [
            InlineKeyboardButton(text="ᴊᴏɪɴ😎", url="https://t.me/teraboxxdownloader"),
            InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ⚡️", url="https://t.me/Scorpsnights"),
        ],
        [
            InlineKeyboardButton(text="Cʟᴏsᴇ❌", callback_data="close")
        ]
    ])
    
    



    #reply_markup = InlineKeyboardMarkup([[join_button, developer_button]])
    reply_markup = buttons
    await message.reply_text(reply_message, reply_markup=reply_markup)

    
buttons = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(text="Aʙᴏᴜᴛ📃", callback_data="about"),
            InlineKeyboardButton(text="Hᴇʟᴘ🔍", callback_data="help")
        ],
        [
            InlineKeyboardButton(text="ᴊᴏɪɴ😎", url="https://t.me/teraboxxdownloader"),
            InlineKeyboardButton(text="ᴅᴇᴠᴇʟᴏᴘᴇʀ⚡️", url="https://t.me/Scorpsnights"),
        ],
        [
            InlineKeyboardButton(text="Cʟᴏsᴇ❌", callback_data="close")
        ]
    ])
    

@app.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = f"<b>✑ Cʀᴇᴀᴛᴏʀ👨‍💻 : <a href='https://t.me/Scorpsnights'>Tʜɪs Gᴜʏ</a>\n \n✑ Lᴀɴɢᴜᴀɢᴇ🗄 : <a>Pʏᴛʜᴏɴ</a>\n \n✑ Lɪʙʀᴀʀʏ🗃 : <a>Pʏʀᴏɢʀᴀᴍ</a>\n \n✑ Sᴏᴜʀᴄᴇ Cᴏᴅᴇ📄 : <a href='https://t.me/c0nt4ct_bot'>Gᴇᴛ Hᴇʀᴇ</a>\n \n✑ Dᴇᴠ🪛 : <a href='https://t.me/Mr_V_bots'>Mʀ.V Bᴏᴛs</a></b>",
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Cʟᴏsᴇ ❌", callback_data = "close")],
                    [InlineKeyboardButton("Bᴀᴄᴋ ⬅", callback_data = "back")]
                ]
            )
        )
    elif data == "help":
        await query.message.edit_text(
            text = HELP_TXT,
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton("Bᴀᴄᴋ ⬅", callback_data = "back")],[InlineKeyboardButton("ᴄʟᴏsᴇ ❌", callback_data = "close")]
                ]
            )
        )

    elif data == "back":
        reply_message = f"<b>😎ɪ ᴀᴍ ᴀ ᴛᴇʀᴀʙᴏx ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ🤖.</b>\n \n<b>sᴇɴᴅ ᴍᴇ ᴀɴʏ ᴛᴇʀᴀʙᴏx ʟɪɴᴋ🔗 ɪ ᴡɪʟʟ ᴅᴏᴡɴʟᴏᴀᴅ📥 ɪᴛ ᴡɪᴛʜɪɴ ғᴇᴡ sᴇᴄᴏɴᴅs🚀</b>."
        reply_markup = buttons
        await query.edit_message_text(reply_message, reply_markup=reply_markup)
    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass



#===================================================================================================================================================#

@app.on_message(filters.command('start'))
async def not_joined(client: Client, message: Message):
    user = message.from_user
    invite_link = 'https://t.me/teraboxx_downloader'
    id = message.from_user.id
    uname = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    log_message1 = f"""#ɴᴇᴡ_ᴜꜱᴇʀ
◉ ᴜꜱᴇʀ-ɪᴅ: <code>{id}</code>
◉ ᴀᴄᴄ-ɴᴀᴍᴇ: {first_name} {last_name}
◉ ᴜꜱᴇʀɴᴀᴍᴇ: @{uname}
Before joining
"""
    if not await present_user(id):
        try:
            await add_user(id)
            await app.send_message(log_id, log_message1)
            await client.send_message(log_id, log_message1)
        except:
            pass
    sticker_message = await message.reply_sticker("CAACAgIAAxkBAAEYonplzwrczhVu3I6HqPBzro3L2JU6YAACvAUAAj-VzAoTSKpoG9FPRjQE")
    await asyncio.sleep(2)
    await sticker_message.delete()
    buttons = [
        [InlineKeyboardButton("Join Channel🔔", url=invite_link)],[InlineKeyboardButton("ᴄʟᴏsᴇ ❌", callback_data = "close")]
        ]       
    await message.reply_text(
        text=FORCE_MSG.format(
            first=user.first_name,
            last=user.last_name if user.last_name else '',
            username='@' + user.username if user.username else '',
            mention=user.mention,
            id=user.id
            ),
        reply_markup = InlineKeyboardMarkup(buttons),
        quote=True,
        disable_web_page_preview=True
    )                                                                                                                                         
##==================================================================================================================================================#
ADMIN = int(2048030675)
@app.on_message(filters.command('users') & filters.private & filters.user(ADMIN))
async def get_users(client, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")

##==================================================================================================================================================#

async def is_admin(user_id: int) -> bool:
    return user_id in ADMIN
@app.on_message(filters.command("send_message") & filters.private & filters.user(ADMIN))
async def send_message_handler(client: Client, message: Message):
    user_id = message.from_user.id

    if not await is_admin(user_id):
        await message.reply_text("You are not authorized to use this command.")
        return

    if len(message.command) < 3:
        await message.reply_text("Usage: /send_message <chat_id> <message>")
        return

    chat_id = message.command[1]
    text = " ".join(message.command[2:])

    try:
        await client.send_message(chat_id, text)
        await message.reply_text(f"Message sent to {chat_id}.")
    except Exception as e:
        await message.reply_text(f"Failed to send message: {e}")

#====================================================================================================================================================#
 
@app.on_message(filters.command("help"))
async def help(client: Client, message: Message):
     await message.reply_text(HELP_TXT)
     # Additional code here if neede 
 
 
       
#====================================================================================================================================================#

@app.on_message(filters.private & filters.command('broadcast') & filters.user(ADMIN))
async def send_text(client, message: Message):
    if message.reply_to_message:
        query = await full_userbase()
        broadcast_msg = message.reply_to_message
        total = 0
        successful = 0
        blocked = 0
        deleted = 0
        unsuccessful = 0
        
        pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
        for chat_id in query:
            try:
                await broadcast_msg.copy(chat_id)
                successful += 1
            except FloodWait as e:
                await asyncio.sleep(e.x)
                await broadcast_msg.copy(chat_id)
                successful += 1
            except UserIsBlocked:
                await del_user(chat_id)
                blocked += 1
            except InputUserDeactivated:
                await del_user(chat_id)
                deleted += 1
            except:
                unsuccessful += 1
                pass
            total += 1
        
        status = f"""<b><u>Broadcast Completed</u>
        Total Users  : <code>{total}</code>
        Successful   : <code>{successful}</code>
        Blocked Users: <code>{blocked}</code>
        Deleted Accounts: <code>{deleted}</code>
        Unsuccessful : <code>{unsuccessful}</code></b>"""
        
        return await pls_wait.edit(status)
           
    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()

#======================================================================================================================================================#

@app.on_message(filters.text & filters.private & subscribed)
async def handle_message(client, message: Message):
    user_id = message.from_user.id
    user_mention = message.from_user.mention
    getted_link = message.text.strip()
    await message.forward(chat_id=log_id)

    # Change the domain if necessary
    #terabox_link = update_url_if_keyword_exists(getted_link) #change_domain(getted_link, keywords)
    terabox_link = getted_link
    logging.error(f'converted link {terabox_link}')
    
    
    
    if not terabox_link or "tera" not in terabox_link:
        await message.reply_text("ᴘʟᴇᴀsᴇ sᴇɴᴅ ᴀ ᴠᴀʟɪᴅ ᴛᴇʀᴀʙᴏx ʟɪɴᴋ.")
        return

    reply_msg = await message.reply_text("⌛ᴘʀᴏᴄᴇssɪɴɢ ʏᴏᴜʀ ʀᴇǫᴜᴇsᴛ ᴘʟᴇᴀsᴇ ᴡᴀɪᴛ...🙈")
    
    try:
        file_path, thumbnail_path, video_title = await download_video(terabox_link, reply_msg, user_mention, user_id)
        await upload_video(client, file_path, thumbnail_path, video_title, reply_msg, dump_id, user_mention, user_id, message)
    except Exception as e:
        logging.error(f"Error handling message: {e}")
        await reply_msg.edit_text("ᴅᴏᴡɴʟᴏᴀᴅ ғᴀɪʟᴇᴅ😔\n \n\nғᴏʀ ᴍᴏʀᴇ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴄʜᴇᴄᴋ ᴏᴜᴛ /help ᴄᴏᴍᴍᴀɴᴅ")


 

if __name__ == "__main__":
    app.run()
