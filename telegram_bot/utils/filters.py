from pyrogram import filters
from utils.connection import connection as con
from utils.utils import join_checker



async def bot_is_active(_ , __ , msg):
        if con and con.setting:
            if con.setting.is_active :
                return True
        return False
    



async def bot_not_active(_ , __ , msg ):
        
        if con and con.setting :
            if con.setting.is_active == False:
                return True
            else:return False
        return True



async def user_not_active(_ , __ , msg ):
        if con :
            first_name = str(msg.from_user.first_name if msg.from_user.first_name is not None else '')
            last_name = str(msg.from_user.last_name if msg.from_user.last_name is not None else '')
            full_name =  f'{str(first_name)} {str(last_name)}'
            chat_id  = int(msg.from_user.id )
            user = con.user(chat_id=chat_id , full_name=full_name)
            if user and user.is_active is False :
                return True
            else :return False
        return False
    
        
async def user_is_active(_ , __ , msg ):
        if con :
            first_name = str(msg.from_user.first_name if msg.from_user.first_name is not None else '')
            last_name = str(msg.from_user.last_name if msg.from_user.last_name is not None else '')
            full_name =  f'{str(first_name)} {str(last_name)}'
            chat_id  = int(msg.from_user.id )
            user = con.user(chat_id=chat_id , full_name=full_name)
            if user and user.is_active :
                return True
            else :return False
        return False
    

async def user_is_join(_ , cli , msg ):
    if con and con.setting :
        channels = con.setting.channels
        is_join = await join_checker(cli , msg , channels)
        if not is_join : return True
        else :return False
    else :return False



async def user_not_join(_ , cli , msg ):
    if con and con.setting :
        channels = con.setting.channels
        is_join = await join_checker(cli , msg , channels)
        if not is_join : return False
        else :return True
    else :return False


user_not_join=filters.create(user_not_join)
user_is_join = filters.create(user_is_join)
user_is_active = filters.create(user_is_active)
user_not_active = filters.create(user_not_active)
bot_not_active = filters.create(bot_not_active)
bot_is_active = filters.create(bot_is_active)

