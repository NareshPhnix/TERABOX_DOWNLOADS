import re 
import os
from os import environ
import moviepy
import asyncio
import logging
from pyrogram import Client, filters, errors
from pyrogram.types import Message
from pyrogram.enums import ChatMemberStatus
from config import KEYWORDS, FSUB_ID
from dotenv import load_dotenv
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors import FloodWait
import pyrogram.utils
from urllib.parse import urlparse, urlunparse, ParseResult
import os
from moviepy.editor import VideoFileClip
from pyrogram.errors import RPCError
import hachoir
from hachoir.parser import createParser
from hachoir.metadata import extractMetadata
from hachoir.core import config as hachoir_config


load_dotenv('sconfig.env', override=True)
logging.basicConfig(level=logging.INFO)

pyrogram.utils.MIN_CHANNEL_ID = -1002249393777
pyrogram.utils.MIN_CHANNEL_ID = -1002133701521
pyrogram.utils.CHANNEL_ID = -1002133701521
pyrogram.utils.MIN_CHANNEL_ID = -1002149484754
pyrogram.utils.CHANNEL_ID = -1002149484754

#pyrogram.utils.MIN_CHANNEL_ID = -1002249393777
#pyrogram.utils.CHANNEL_ID = -1002249393777

id_pattern = re.compile(r'^.\d+$')

ADMINS = [int(admin) if id_pattern.search(
        admin) else admin for admin in os.environ.get('ADMINS', '2048030675').split()]

fsub_id = os.environ.get('FSUB_ID', '')
if len(fsub_id) == 0:
    logging.error("FSUB_ID variable is missing! Exiting now")
    exit(1)
else:
    fsub_id = int(fsub_id)

admins = os.environ.get('ADMINS', '')
if len(admins) == 0:
    logging.error("ADMINS variable is missing! Exiting now")
    exit(1)
else:
    admins = int(admins)

keywords = os.getenv("KEYWORDS", '').split(',')



#====================================================================================================================================================#


async def is_subscribed(filter, client, update):
    if not fsub_id:
        return True
    user_id = update.from_user.id
    logging.warning(f"{user_id} Is The using the bot now") 
    
    if user_id is int(admins):
        return True
    try:
        member = await client.get_chat_member(chat_id = fsub_id, user_id = user_id)
    except UserNotParticipant:
        return False

    if not member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR, ChatMemberStatus.MEMBER]:
        return False
    else:
        return True



subscribed = filters.create(is_subscribed)

#====================================================================================================================================================#
keywords = KEYWORDS
# Function to change the domain
def change_domain(url, new_domain):
    # Parse the URL
    parsed_url = urlparse(url)
    new_domain = "www.freeterabox.com"
    
    # Replace the netloc (domain) with the new domain
    new_netloc = new_domain
    new_url = parsed_url._replace(netloc=new_netloc)
    
    # Reconstruct the URL with the new domain
    return urlunparse(new_url)

def update_url_if_keyword_exists(url):
    # Check if the URL contains any of the keywords
    for keyword, new_domain in keywords.items():
        if keyword in url:
            return change_domain(url, new_domain)
    
    # Return the original URL if no keywords are found
    return url
#-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=----=---=-=-=-=-=-=#

#def get_video_duration(file_path):
#    with VideoFileClip(file_path) as video:
#        return video.duration
    
def get_video_duration(file_path):
    parser = createParser(file_path)
    if not parser:
        print(f"Unable to parse file: {file_path}")
        return None
    
    with parser:
        metadata = extractMetadata(parser)
        if not metadata:
            print(f"Unable to extract metadata from file: {file_path}")
            return None
        
        duration = metadata.get('duration')
        if duration:
            return duration.total_seconds()
        else:
            print(f"No duration found in metadata for file: {file_path}")
            return None




def format_duration(duration):
    hours, rem = divmod(duration, 3600)
    minutes, seconds = divmod(rem, 60)
    return "{:0>2}:{:0>2}:{:05.2f}".format(int(hours), int(minutes), seconds)


#-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=-==-=-=-=-=-=-=-=-=-=-=-=----=---=-=-=-=-=-=#
