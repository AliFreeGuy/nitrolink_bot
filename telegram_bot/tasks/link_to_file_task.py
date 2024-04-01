from celery import Celery
from pyrogram import Client
import redis
import os 
from datetime import datetime
import os
import redis
from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,InlineKeyboardButton , KeyboardButton)
import requests
from urllib.parse import unquote
from datetime import datetime
from dotenv import load_dotenv
import yt_dlp



load_dotenv(override=True)

API_HASH = os.getenv("API_HASH")
API_ID = os.getenv("API_ID")
BOT_TOKEN = os.getenv("BOT_TOKEN")
PLUGINS = dict(root=os.getenv("PLUGINS_ROOT"))
PROXY = {"scheme": os.getenv("PROXY_SCHEME"),
         "hostname": os.getenv("PROXY_HOSTNAME"),
         "port": int(os.getenv("PROXY_PORT"))}
API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")
DEBUG = os.getenv('DEBUG')
CACHE_TTL = os.getenv('CACHE_TTL')
UPDATE_SEC = int(os.getenv('UPDATE_SEC'))
BOT_SESSION_STRING = os.getenv('BOT_SESSION_STRING')
REIDS_DB = int(os.getenv('REDIS_DB'))





r = redis.Redis(host='localhost' , port=6379 , db=REIDS_DB , decode_responses=True  , soft_time_limit=10000)
app = Celery('link_to_file' , backend='redis://localhost:6379/6' , broker='redis://localhost:6379/6')
app.conf.update(
    task_serializer='json',
    result_serializer='json',
    accept_content=['json',],  
    worker_concurrency=3,
    worker_prefetch_multiplier=1,
)




@app.task(name='link_to_file.url_downloader', bind=True, default_retry_delay=1)
def url_downloader(self , data ):


    task_id = self.request.id
    url = data['url']
    if DEBUG == 'True' :bot = Client('test'  , api_id=API_ID , api_hash=API_HASH , session_string=BOT_SESSION_STRING  , proxy=PROXY)
    else : bot = Client('test'  , api_id=API_ID , api_hash=API_HASH , session_string=BOT_SESSION_STRING )
    filename = None 
    work_dir = 'workdir'
    base_dir = os.getcwd()
    task_id = self.request.id
    directory_name = str(task_id)
    full_path = os.path.join(work_dir, directory_name)
    os.makedirs(full_path, exist_ok=True)
    file_path =  f'{base_dir}/{work_dir}/{directory_name}/'

    def progress_hook(d):
        global dl_progress
        global fp
        if d["status"] == "downloading" and d["total_bytes"] > 0:
            dl_progress = int(d["downloaded_bytes"] / d["total_bytes"] * 100)
            print(f"{dl_progress}".split(' ')[0])
            progress_str = progressbar(total=200 , current=dl_progress  , task_id=task_id)
            if progress_str['is_update']  == 'True' :
                fp = d['filename']  # تنظیم مسیر فایل
                with bot :
                    try :
                        text  = f'`{data["message_text"]}\n\n{progress_str["text"]}`'
                        bot.edit_message_text(chat_id=int(data['chat_id']) , message_id=int(data['message_id']) , text=text)
                    except :pass


    ydl_opts = {
        'progress_hooks': [progress_hook],
        'outtmpl': f'{file_path}%(title)s.%(ext)s'
    }


    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print('********************** DOWNLOADED ***********************************')

    try :
        with bot :
                    def progress(current, total):
                        progress_data = int(float(f"{current * 100 / total:.1f}"))
                        progress_str = progressbar(total=200 , current=progress_data +100 , task_id=task_id)
                        if progress_str['is_update'] == 'True' :
                            try :
                                text  = f'`{data["message_text"]}\n\n{progress_str["text"]}`'
                                bot.edit_message_text(chat_id=int(data['chat_id']) , message_id=int(data['message_id']) , text=text)
                            except :pass
                    
                    
                    bot.send_document(chat_id=int(data['chat_id']) , document=fp , progress=progress , )
                    bot.delete_messages(chat_id=int(data['chat_id']) , message_ids=int(data['message_id']))
                    delet_dir(file_path)
    except Exception as e :
        print(e)
        delet_dir(file_path)

    delet_dir(file_path)

                



def delet_dir(path):
    try :
        os.system(f"rm -rf {path}")
    except Exception as e : print('delete dir ' , str(e))
    


def progressbar(current, total, task_id=None):
    percentage = current * 100 // total
    progress_bar = ""
    for i in range(20):
        if percentage >= (i + 1) * 5:
            progress_bar += "█"
        elif percentage >= i * 5 + 2:
            progress_bar += "▒"
        else:
            progress_bar += "░"
    date = datetime.now()
    progress_data = {'progress': progress_bar, 'percentage': percentage, 'text': f"{progress_bar} {str(int(percentage))}", 'date': str(date)}
    if not r.exists(task_id):
        r.hmset(task_id, progress_data)
        progress_data['is_update'] = 'True'
    elif r.exists(task_id):
        if int(float(r.hgetall(task_id)['percentage'])) != percentage:
            p = r.hgetall(task_id)
            last_pdate = datetime.strptime(p['date'], '%Y-%m-%d %H:%M:%S.%f')
            time_difference = date - last_pdate
            seconds_difference = time_difference.total_seconds()
            if int(seconds_difference) >= UPDATE_SEC:
                progress_data['is_update'] = 'True'
                r.hmset(task_id, progress_data)
            else:
                progress_data['is_update'] = 'False'
        else:
            r.hmset(task_id, progress_data)
            progress_data['is_update'] = 'False'
    return progress_data
