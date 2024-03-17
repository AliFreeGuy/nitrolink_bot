import requests
from django.conf import settings
from requests.exceptions import Timeout
def send_message(chat_id , message, bot_token ):
        try :
                url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
                payload = {'chat_id': chat_id,'text': message}
    
                try:
                    response = requests.post(url, data=payload, timeout=1)
                    response.raise_for_status() 
                    return response
                except Timeout:
                    print("Timeout occurred. Message was not sent within 1 second.")
                    return None
                except requests.exceptions.RequestException as e:
                    print(f"An error occurred: {e}")
                    return None
        except Exception as e :
            return e




