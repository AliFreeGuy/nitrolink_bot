from pyrogram import Client ,filters
from dotenv import load_dotenv
import os


load_dotenv(override=True)
session_string = os.getenv('SESSION_STRING')
API_HASH = os.getenv("API_HASH")
API_ID = os.getenv("API_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")
PLUGINS = dict(root=os.getenv("PLUGINS_ROOT"))
PROXY = {"scheme": os.getenv("PROXY_SCHEME"),
         "hostname": os.getenv("PROXY_HOSTNAME"),
         "port": int(os.getenv("PROXY_PORT"))}
DEBUG = os.getenv('DEBUG')
BOT_USERNAME = os.getenv('BOT_USERNAME')
INTERMEDIATE_ACCOUNT = os.getenv('INTERMEDIATE_ACCOUNT')
INTERMEDIATE_BOT = os.getenv('INTERMEDIATE_BOT')


if DEBUG == 'True' :
    bot = Client('listner' , api_hash=API_HASH , api_id=API_ID , session_string=session_string , proxy=PROXY)
else :
    bot = Client('listner' , api_hash=API_HASH , api_id=API_ID , session_string=session_string )

@bot.on_message(filters.chat(str(BOT_USERNAME)))
async def bot_listner(client , message ):
    if message.media :await message.copy(INTERMEDIATE_BOT)
bot.run()
    