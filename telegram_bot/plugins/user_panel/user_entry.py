from pyrogram import Client   , filters
from utils import filters as f 
from utils.connection import connection as con
from utils.utils import join_checker
from utils import btn




@Client.on_message(filters.private & f.bot_not_active , group=0)
async def bot_not_active(client , message):
      if con and con.setting :
            await client.send_message(message.from_user.id , text = con.setting.not_active_text)


# @Client.on_message()
# async def test(client , message ):
#        print(message)
      # data = await client.get_chat_member(-1004147544522 , message.from_user.id )
      # print(data )


@Client.on_message(filters.private & f.user_not_active , group=0)
async def user_not_active(client , message):
            if con and con.setting :
                  await client.send_message(message.from_user.id , text =con.setting.user_not_active_text)




@Client.on_message(filters.private & f.user_not_join , group=0)
async def user_not_join(client , message ):
      channels = con.setting.channels
      not_join_channels = await join_checker(client , message ,channels)
      if not_join_channels :
            await client.send_message(message.from_user.id   , text = con.setting.join_channel_text  , reply_markup = btn.join_channels_url(not_join_channels))