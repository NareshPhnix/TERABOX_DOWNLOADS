import os
import re

BOT_TOKEN = "7458046887:AAHJ0_DHcI5-4CfwcyfCsVsTYecRE2EhPRI"

TELEGRAM_API = "28192191"

TELEGRAM_HASH = "663164abd732848a90e76e25cb9cf54a"

id_pattern = re.compile(r'^.\d+$')

ADMINS = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMINS', '1676244457').split()]
#Bot's usernmae without @
BOT_USERNAME = "https://t.me/teraboxxdownloader"

#KEYWORDS = ['nephobox', 'terabox', 'teraboxapp', '1024terabox', '1024tera']
KEYWORDS = {
    'terabox': 'www.terabox.com',
    '1024tera': 'www.1024tera.com',
    'terashare': 'www.teraboxshare.com',
    'teraboxlink': 'www.teraboxlink.com',
    '1024terabox': 'www.1024terabox.com',
    'teraboxsharelink': 'www.terasharelink.com',
    'teraboxapp': 'www.teraboxapp.com',
    'teraboxshare': 'www.teraboxshare.com',
    'terasharelink': 'www.terasharelink.com',
    'nephobox': 'www.nephobox.com'
}

FORCE_MSG = "ʜᴇʟʟᴏ 😊 {first}\n\n<b>Yᴏᴜ ɴᴇᴇᴅ ᴛᴏ Jᴏɪɴ ɪɴ ᴍʏ Cʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴍᴇ Kɪɴᴅʟʏ Pʟᴇᴀsᴇ Jᴏɪɴ ᴍʏ Cʜᴀɴɴᴇʟ</b>"

FSUB_ID = "-1002232462602"



DUMP_CHAT_ID = "-1002212612017"

DB_URI = "mongodb+srv://phoenix:Mongo.12345nht@cluster123.1mvajso.mongodb.net/?retryWrites=true&w=majority&appName=cluster123"

DB_NAME = "tbcluster"

WAIT_MSG = "Please Wait....."

REPLY_ERROR = "Reply to a message"

LOG_ID = "-1002220732120"

LOG_TEXT = """#ɴᴇᴡ_ᴜꜱᴇʀ

◉ ᴜꜱᴇʀ-ɪᴅ: <code>{id}</code>
◉ ᴀᴄᴄ-ɴᴀᴍᴇ: {first_name} {last_name}
◉ ᴜꜱᴇʀɴᴀᴍᴇ: @{uname}"""

HELP_TXT = f"""<b>Hᴏᴡ ᴛᴏ Usᴇ?💡</b>
\n<b>Jᴏɪɴ ᴛʜᴇ ᴄʜᴀɴɴᴇʟ ғɪʀsᴛ ᴀɴᴅ ᴛʜᴇɴ sᴇɴᴅ ᴀɴʏ ᴛᴇʀᴀʙᴏx ʟɪɴᴋ ᴛᴏ ᴛʜᴇ ʙᴏᴛ</b>

\n<b>Rᴇᴀsᴏɴ ғᴏʀ Dᴏᴡɴʟᴏᴀᴅ Fᴀɪʟᴇᴅ🚩</b>\n
   \n<b>♦ Mᴀʏ ʙᴇ ᴅᴜᴇ ᴛᴏ ᴛʜᴇ Fɪʟᴇ sɪᴢᴇ📁</b> 
   \n<b>♦ Mᴜʟᴛɪᴘʟᴇ Fɪʟᴇs🗂 ɪɴ ᴛʜᴇ ʟɪɴᴋ </b>
   \n<b>♦ ᴅᴜᴇ ᴛᴏ Tᴇʀᴀʙᴏx Eʀʀᴏʀ🚧</b>
   \n<b>♦ Sᴇʀᴠᴇʀ ᴛɪᴍᴇᴏᴜᴛ ᴇʀʀᴏʀ</b>
   \n<b>♦ Eʀʀᴏʀ ᴡʜɪʟᴇ ɢᴇᴛᴛɪɴɢ ʀᴇsᴘᴏɴsᴇ ғʀᴏᴍ sᴇʀᴠᴇʀ</b>

\n<b>ᴀɴʏ ɪssᴜᴇs ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴛʜᴇ ᴀʙᴏᴠᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ᴠɪᴀ</b> @Feedsstore_Bot"""
