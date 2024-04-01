from pyrogram import Client   , filters
from utils.connection import connection as con
from utils import filters as f 
from utils import btn , text
from utils.utils import url_getter , get_link_to_file_db , add_link_to_file_db , alert
from utils.link_to_file import get_url_info
import redis
import random
from tasks import link_to_file_task



@Client.on_message(
                    filters.private &
                    f.user_is_active &
                    f.bot_is_active & f.user_is_join &
                    filters.regex('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+') ,
                    group=2)
async def link_to_file_handler(client , message ):
    url = url_getter(message.text)
    data = get_url_info(url=url[0])


    loading_data = await client.send_message(
    chat_id=message.chat.id,
    text=text.loading_text,
    reply_to_message_id=message.id
)
    
    if data is not None and data['file_size']:
        data['chat_id'] = message.from_user.id 
        data['message_id'] = loading_data.id
        data['url'] = url[0]
        key = f'link_to_file:{str(message.from_user.id)}:{str(random.randint(0,999999))}'
        data['key'] = key
        val = data
        add_link_to_file_db(key , val )
        await loading_data.edit_text(text = text.file_info(data['file_name'] , data['file_size_str']) , reply_markup = btn.get_file(key))
    else :await loading_data.edit_text(text = text.error_loading_text)




@Client.on_callback_query(f.user_is_active  & f.bot_is_active , group=2)
async def callback_link_to_file_handler(client , call ):

    if call.data.startswith('link_to_file'):
        call_data = get_link_to_file_db(call.data)
        call_data['message_text']  =call.message.text
        

        if float(call_data['file_size'])<=2000.0 :
            volume_usage = con.volume_usage(user=call.from_user.id , 
                                            operation_type='increase' ,
                                            volume=float(call_data['file_size']),
                                            bot_status='link_to_file'
                                            )
            if volume_usage :


                await call.edit_message_text(text.progres_link_to_file(name_size=call.message.text))
                link_to_file_task.url_downloader.delay(call_data)


            else : await alert(client , call , msg=text.max_size_limit)
        else : await alert(client , call , msg=text.file_limit_2gb)