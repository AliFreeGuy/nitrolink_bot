
from pyrogram.errors import UserNotParticipant
import jdatetime
import re
import requests
from tqdm import tqdm
from urllib.parse import unquote
import redis
from config import REDIS_DB



r = redis.Redis(host='localhost' , port=6379 , db=REDIS_DB , decode_responses=True)

async def join_checker(cli , msg , channels ):
    my_channels = []
    not_join = []
    for channel in channels :
        data = channel.split(' ')
        if len(data) == 2 : my_channels.append({'link' : data[0] , 'chat_id' : data[1]})
    for i in my_channels : 
        try :data = await cli.get_chat_member(int(i['chat_id']), msg.from_user.id )
        except UserNotParticipant :not_join.append(i['link'])
        except Exception as e  : print(e)
    return not_join

    

async def alert(client ,call , msg = None ):
    try :
        if msg is None : await call.answer('خطا لطفا دوباره تلاش کنید', show_alert=True)
        else : await call.answer(msg , show_alert = True)
    except Exception as e : print('alert ' , str(e))
    
   


def convert_to_gigabytes(megabytes):
    if megabytes != 0 :
        gigabytes = megabytes / 1024
        return f"{gigabytes:.1f} GB"
    else :return '0.0 GB'
        


def jdate(date_miladi):
        try :date_time = jdatetime.datetime.strptime(date_miladi, "%Y-%m-%dT%H:%M:%S.%fZ")
        except : date_time = jdatetime.datetime.strptime(date_miladi, "%Y-%m-%dT%H:%M:%SZ")
        date_shamsi = jdatetime.datetime.fromgregorian(datetime=date_time).replace(hour=0, minute=0, second=0, microsecond=0)
        current_date_shamsi = jdatetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)
        remaining_days = (date_shamsi - current_date_shamsi).days
        date = date_shamsi.strftime('%Y-%m-%d').split('-')
        date = f'{date[2]}-{date[1]}-{date[0]}'
        result = {
            'date': date,
            'day': remaining_days
        }
        return result



def url_getter(text ):
    pattern = r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
    matches = re.findall(pattern, text , re.MULTILINE | re.IGNORECASE)
    return matches




def add_link_to_file_db(key , val ):
    r.hmset(key , val )
    return r.hgetall(key)


def get_link_to_file_db(key):
    return r.hgetall(key)