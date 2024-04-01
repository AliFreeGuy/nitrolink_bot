from config import API_HASH , API_ID , BOT_TOKEN , PROXY , PLUGINS , DEBUG
from pyrogram import Client



if DEBUG  == 'True': 
        bot = Client(
                name = "bot",
                api_id=API_ID , 
                api_hash=API_HASH , 
                bot_token=BOT_TOKEN , 
                proxy=PROXY ,
                plugins=PLUGINS)
else :
        bot = Client(
                name = "bot",
                api_id=API_ID , 
                api_hash=API_HASH , 
                bot_token=BOT_TOKEN , 
                plugins=PLUGINS)



if __name__ == '__main__' : 

        bot.run()
  
