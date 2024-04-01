from pyrogram import Client   , filters
from utils.connection import connection as con
from utils import filters as f 
from utils import btn , text
from utils.utils import jdate

@Client.on_message(filters.private & f.user_is_active & f.bot_is_active & f.user_is_join, group=1)
async def base_command_handler(client , message ):

    if message.text and con.setting: 
        chat_id  = message.from_user.id 


        if message.text == '/start' : 
            await client.send_message(chat_id , text = con.setting.start_text)

        elif message.text == '/help' : 
            await client.send_message(chat_id , text = con.setting.help_text)

        elif message.text == '/support' :
            await client.send_message(chat_id , text = con.setting.support_text)

        elif message.text == '/plans' : 
            await plans_handler(client , message)

        elif message.text == '/profile' : 
            await profile_handler(client , message)
        



async def plans_handler(client , message):
    if con and con.plans : 
        await client.send_message(message.from_user.id , text = con.setting.plans_text , reply_markup = btn.plans_btn(con.plans , support_id=con.setting.support_id))
     


async def profile_handler(client , message):
    user = con.get_user(message.from_user.id )
    await client.send_message(message.from_user.id , 
                              text = text.user_profile(user , message.from_user.id ))
    