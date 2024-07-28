import os
import re

BOT_TOKEN = ""

TELEGRAM_API = ""

TELEGRAM_HASH = ""

id_pattern = re.compile(r'^.\d+$')

ADMINS = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMINS', '').split()]
#Bot's usernmae without @
BOT_USERNAME = ""

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

FSUB_ID = ""



DUMP_CHAT_ID = ""

DB_URI = ""

DB_NAME = "tbcluster"

WAIT_MSG = "Please Wait....."

REPLY_ERROR = "Reply to a message"

LOG_ID = ""

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

\n<b>ᴀɴʏ ɪssᴜᴇs ᴏᴛʜᴇʀ ᴛʜᴀɴ ᴛʜᴇ ᴀʙᴏᴠᴇ ᴄᴏɴᴛᴀᴄᴛ ᴀᴅᴍɪɴ ᴠɪᴀ</b> @c0nt4ct_bot"""