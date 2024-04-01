from utils.utils import jdate , convert_to_gigabytes
from utils.connection import connection as con


loading_text = 'در حال بارگذاری ...'
error_loading_text = 'خطا لطفا بعدا تلاش کنید'
file_limit_2gb = 'حجم فایل باید کمتر از 2GB باشد'
max_size_limit = 'محدودیت حجمی !'
user_not_volume = 'شما حجم کافی برای تبدیل این فایل ندارید !'




def user_profile(user , chat_id ):
    zero_gb = '0.0 GB'
    if user.sub.is_active :
        text = f'''
شناسه کاربری : `{str(chat_id)}`

حجم مانده فایل به لینک : `{convert_to_gigabytes(user.sub.file_to_link_volume)}`

حجم مانده لینک به فایل : `{convert_to_gigabytes(user.sub.link_to_file_volume)}`

تاریخ پایان اشتراک : `{str(jdate(user.sub.expiry)['date'])}`

'''
        return text

    else :
        
        return f'''
شناسه کاربری : `{str(chat_id)}`

حجم مانده فایل به لینک : `{zero_gb}`

حجم مانده لینک به فایل : `{zero_gb}`

تاریخ پایان اشتراک : `0`

'''
    




# def user_profile(user , chat_id ):
#     zero_gb = '0.0 GB'
#     if user.sub.is_active :
#         text = f'''
# شناسه کاربری : `{str(chat_id)}`

# حجم باقی مانده فایل به لینک : `{convert_to_gigabytes(user.sub.file_to_link_volume)}`
# حجم استفاده شده روزانه فایل به لینک : `{convert_to_gigabytes(user.sub.file_to_link_usage_to_day)}`

# حجم باقی مانده لینک به فایل : `{convert_to_gigabytes(user.sub.link_to_file_volume)}`
# حجم استفاده شده روزانه فایل به لینک : `{convert_to_gigabytes(user.sub.link_to_file_usage_to_day)}`

# تاریخ پایان اشتراک : `{str(jdate(user.sub.expiry)['date'])}`

# '''
#         return text

#     else :
        
#         return f'''
# شناسه کاربری : `{str(chat_id)}`

# حجم باقی مانده فایل به لینک : `{zero_gb}`
# حجم استفاده شده روزانه فایل به لینک : `{zero_gb}`

# حجم باقی مانده لینک به فایل : `{zero_gb}`
# حجم استفاده شده روزانه فایل به لینک : `{zero_gb}`

# تاریخ پایان اشتراک : `0`

# '''
    


def file_info(name , size ):
    text = f'''`
🗂 {name}
📥 {size}`'''
    
    return text

def progres_link_to_file(name_size  , progress=0 ):
    zero_progres = '░░░░░░░░░░░░░░░░░░░░ 0'
    text = f'''`
{name_size}

{zero_progres if progress == 0 else progress}`'''
    return text
    


