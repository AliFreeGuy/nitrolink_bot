# from pyrogram import Client
# import os
# from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,InlineKeyboardButton , KeyboardButton)
# API_HASH='5fb64e86e605887fa0197475f6a4896c'
# API_ID=14206072
# BOT_TOKEN='6045204910:AAHoiiyR8kk6PWaKW-n4LfyeqslheA6GMPY'
# DEBUG =True
# BOT_SESSION_STRING = 'BAGtrjYAh-9YMYaGcCStTeefQwpfCV3OcKhHnLtBqL_RFrizwAc6qtZVa6Zo_6wZa6EM1h44ZjWKCbgBDVjrkTxWo7XB2ARLOA3S2C10fI2xY3vJzWYBMeC9tc0WxSPn2kC8k1oed1Fr0S51KUQdYoVDvj2fyLuvrJw9G-7HB3RZMg6ic7wTG5r9lsxaLFt_8xtf6bYdwoU-140s-hgXzYAso1YaNRHf_ZcUovWidS49DgDuNJ4TmPRgOQKfDAQItbFQVI3ZA4hXccNSjLjmqrDClFMpaDja4mXAszBZkCd1YYJ9nhypuCRjNac1x5hYVsSgOt_QtwLelQFFq0_4MddgGXELrgAAAAFoUoGuAQ'
# proxy = {"scheme": "socks5","hostname": "127.0.0.1","port": 1080,}



# if DEBUG :bot = Client('test'  , api_id=API_ID , api_hash=API_HASH , session_string=BOT_SESSION_STRING , proxy=proxy)
# else : bot = Client('test'  , api_id=API_ID , api_hash=API_HASH , session_string=BOT_SESSION_STRING )




# with bot :
#         bot.send_document(chat_id='accroot' , document='/home/freeguy/Desktop/filetolink/bot_project/bot/tasks/workdir/046c8078-b815-4cf5-ba9b-9e1eec88b950/f.txt')

import mimetypes

# لینک دانلود شما
import mimetypes
import os.path

from urllib.parse import urlparse
import mimetypes

# لینک دانلود شما
download_link = "https://dl.roadmusics.ir/Music/1402/12/Hichkas%20%26%20Poobon/Hichسیببkas%20%20%20Poobon%20-%20Har%20Ye%20Rooz%20%28320%29.mp3"

# دریافت تمام اطلاعات MIME از کتابخانه mimetypes
mimetypes.init()

# ساخت دیکشنری از نوع MIME به پسوندهای مربوطه
mime_to_extension = {}
for mime_type, extension in mimetypes.types_map.items():
    mime_to_extension.setdefault(mime_type, []).append(extension)

# دریافت اطلاعات از لینک دانلود
parsed_url = urlparse(download_link)

# یافتن نوع MIME مربوط به لینک دانلود
mime_type, encoding = mimetypes.guess_type(download_link)

if mime_type:
    print("نوع MIME:", mime_type)
    if mime_type in mime_to_extension:
        extensions = mime_to_extension[mime_type]
        print("پسوندهای ممکن:")
        for extension in extensions:
            print("-", extension)
    else:
        print("پسوندهای ممکن برای این نوع MIME یافت نشد.")
else:
    print("نوع MIME قابل تشخیص نیست.")

# استخراج اسم فایل از آدرس URL
file_name = parsed_url.path.split("/")[-1]
print("نام فایل:", file_name)

















































































# import requests
# from urllib.parse import unquote
# from datetime import datetime




# from datetime import datetime
# import redis
# import random
# # اتصال به دیتابیس Redis
# r = redis.StrictRedis(host='localhost', port=6379, db=0 , decode_responses=True)
# update_sec = 2

# def progressbar(current, total):
#     percentage = current * 100 // total
#     progress_bar = ""
#     for i in range(20):
#         if percentage >= (i + 1) * 5:
#             progress_bar += "█"
#         elif percentage >= i * 5 + 2:
#             progress_bar += "▒"
#         else:
#             progress_bar += "░"
#     progress_data = {'progress': progress_bar, 'percentage': percentage, 'text': f"{progress_bar} {percentage}"}
#     return progress_data


# def progressbar(current, total, task_id=None):
#     percentage = current * 100 // total
#     progress_bar = ""
#     for i in range(20):
#         if percentage >= (i + 1) * 5:
#             progress_bar += "█"
#         elif percentage >= i * 5 + 2:
#             progress_bar += "▒"
#         else:
#             progress_bar += "░"
#     date = datetime.now()
#     progress_data = {'progress': progress_bar, 'percentage': percentage, 'text': f"{progress_bar} {percentage}", 'date': str(date)}
#     if not r.exists(task_id):
#         r.hmset(task_id, progress_data)
#         progress_data['is_update'] = 'True'
#     elif r.exists(task_id):
#         if int(float(r.hgetall(task_id)['percentage'])) != percentage:
#             p = r.hgetall(task_id)
#             last_pdate = datetime.strptime(p['date'], '%Y-%m-%d %H:%M:%S.%f')
#             time_difference = date - last_pdate
#             seconds_difference = time_difference.total_seconds()
#             if int(seconds_difference) >= update_sec:
#                 progress_data['is_update'] = 'True'
#                 r.hmset(task_id, progress_data)
#             else:
#                 progress_data['is_update'] = 'False'
#         else:
#             r.hmset(task_id, progress_data)
#             progress_data['is_update'] = 'False'
#     return progress_data




# def download_file(url, filename=None):
#     task_id  = str(random.randint(0 , 99999))
#     response = requests.get(url, stream=True)
#     file_size = int(response.headers.get('content-length', 0))
#     block_size = 1024 * 1024

#     if filename is None:
#         content_disposition = response.headers.get('Content-Disposition')
#         if content_disposition:
#             filename = unquote(content_disposition.split("filename=")[1])
#         else:
#             filename = url.split('/')[-1]

#     downloaded = 0
#     with open(filename, 'wb') as file:
#         for data in response.iter_content(block_size):
#             file.write(data)
#             downloaded += len(data)
#             if downloaded % (block_size * 1) == 0:
#                 percent_done = (downloaded / file_size) * 100 
#                 progress_str = progressbar_with_redis(total=200 , current=percent_done  , task_id=task_id)
#                 if progress_str['is_update'] == 'True' :
#                     print(progress_str)

# url = input("Enter the download link: ")
# filename = input("Enter the filename to save as (leave empty for automatic): ")

# download_file(url, filename.strip() if filename else None)
