from pyrogram import Client , filters
from utils import filters as f
from utils.connection import connection as con
from utils import btn
from utils.utils import join_checker  , alert



@Client.on_callback_query(f.user_is_active  & f.bot_is_active , group=1)
async def callback_query_handler(client , call ):
    router = call.data.split(':')[0]

    if router == 'plans' : 
        await call_plans_handler(client , call )

    elif router == 'join' :
        await joined_handler(client , call )



async def call_plans_handler(client  , call ):
    if con  :
        plans = con.plans
        status = call.data.replace('plans:' , '')
        for plan in plans :
            if status == plan['tag']:
                try :
                    await client.edit_message_text(
                                                chat_id = call.from_user.id ,
                                                message_id = call.message.id ,
                                                text = plan['des']  , reply_markup =btn.plans_btn(plans=plans ,
                                                support_id=con.setting.support_id ) 
                                                    )
                except :pass



async def joined_handler(client , call ):
    if con :

        channels = con.setting.channels
        not_join_channels = await join_checker(client , call ,channels)
        if not_join_channels :
            await client.send_message(call.from_user.id   , text = con.setting.join_channel_text  , reply_markup = btn.join_channels_url(not_join_channels))
            await alert(client , call , 'هنوز که تو کانالا جوین نشدی !')
        else :
            await client.delete_messages(call.from_user.id , call.message.id)
            await client.send_message(call.from_user.id , text = con.setting.start_text)