import redis
import time
import json
import requests
from config import API_KEY, API_URL  , CACHE_TTL  ,REDIS_DB 

class ApiConnection:
    def __init__(self, api_key, url) -> None:
        self.api_key = api_key
        self.url = url
        self.headers = {'Authorization': f'token {self.api_key}'}
        self.r = redis.Redis(host='localhost', port=6379, db=REDIS_DB , decode_responses=True)










    @property
    def setting(self):
      
        last_get_setting = self.r.get('last_get_setting') 
        current_time = time.time()
        if last_get_setting is None or current_time - float(last_get_setting)> CACHE_TTL :
            pattern = 'setting'
            url = self.link_generator(pattern=pattern)
            res =  self.get(url)
            if res and res.status_code == 200 :
                res_data = res.json()
                self.r.set('fl_setting' , json.dumps(res_data) , )
                self.r.set('last_get_setting', current_time)
                return Response(res.json())
            
        else :
            return Response(json.loads(self.r.get('fl_setting')))


    

    @property
    def plans(self):
        last_request_time = self.r.get('last_get_plans')  
        current_time = time.time()
        if last_request_time is None or current_time - float(last_request_time) > CACHE_TTL:
            pattern = 'plans'
            url = self.link_generator(pattern=pattern)
            res = self.get(url)
            if res and res.status_code == 200:
                res_data = res.json()
                self.r.set('fl_plans', json.dumps(res_data))
                self.r.set('last_get_plans', current_time)
                return res_data
        else:
            return json.loads(self.r.get('fl_plans'))
                
 



    def user(self, chat_id, full_name=None):

        last_request_time = self.r.get(f'last_get_user:{str(chat_id)}')  
        current_time = time.time()
        if last_request_time is None or current_time - float(last_request_time) > CACHE_TTL:

            pattern  = 'update_user'
            url = self.link_generator(pattern)
            res = self.post(url , chat_id  , full_name)
            res_raw = res
            if res and res.status_code == 200 :
                res = Response(res.json())
                self.r.set(f'fl_user_data:{str(chat_id)}', json.dumps(res_raw.json()))
                self.r.set(f'last_get_user:{str(chat_id)}', current_time)
                return res
        else :
            return Response(json.loads(self.r.get(f'fl_user_data:{str(chat_id)}')))
        return None 
    


    def get_user(self, chat_id):
        pattern = 'update_user'
        url = self.link_generator(pattern)
        res =self.post(url, chat_id)
        if res.status_code == 200 :
            return Response(res.json())
        return None 
    

    def volume_usage(self , user, operation_type , bot_status ,volume ):
        pattern = 'usage'
        url = self.link_generator(pattern)
        data = {'operation_type' : operation_type , 
                'user' : user , 
                'volume' : volume , 
                'bot_status' : bot_status}
        res = requests.post(url=url ,data = data , headers=self.headers)
        if res.status_code == 200 :
            return True
        return False
        



    def link_generator(self, pattern=None):
        if pattern:
            end_point = self.url.rstrip('/') + f'/file_to_link/api/{pattern}/'
            return end_point
        return None

    def get(self, url):
        res = requests.get(url, headers=self.headers)
        return res

    def post(self, url, chat_id, full_name=None):
        data = {'chat_id': chat_id}
        if full_name:
            data['full_name'] = full_name
        res = requests.post(url, headers=self.headers, data=data)
        return res


class Response:
    def __init__(self, data):
        self.data = data
        if isinstance(data, dict):
            for key, value in data.items():
                if isinstance(value, dict):
                    setattr(self, key, Response(value))
                else:
                    setattr(self, key, value)

    def __str__(self):
        return str(self.data)

    def __getattr__(self, attr):
        raise AttributeError(f"'{type(self).__name__}' object has no attribute '{attr}'")


connection = ApiConnection(api_key=API_KEY, url=API_URL)
