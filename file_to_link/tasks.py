
from celery import shared_task
import time
from file_to_link.models import SendMessageModel
from core.models import BotModel
from file_to_link.utils.telegram_send_message import send_message


@shared_task
def send_message_task(msg_id):
    try :
        msg = SendMessageModel.objects.filter(id = msg_id)
        if msg.exists():
            bot = BotModel.objects.filter(name = 'file_to_link').first()
            if bot :
                msg = msg.first()
                users = msg.user.all()
                for user in users :
                    res = send_message(chat_id=int(user.user.chat_id) , message=msg.message , bot_token=bot.token)
                    time.sleep(0.2)
                return True
    except Exception as e :
        print(e)
    



@shared_task
def send_quick_message(chat_id , message ):
    try :

        bot = BotModel.objects.filter(name = 'file_to_link').first()
        res  = send_message(chat_id=int(chat_id)  , message=message ,bot_token=bot.token)
        print(res)

    except Exception as e :
        return e 