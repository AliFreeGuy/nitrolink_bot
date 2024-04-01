from pyrogram.types import (ReplyKeyboardMarkup, InlineKeyboardMarkup,InlineKeyboardButton , KeyboardButton)


def join_channels_url(channels):
    persian_numbers = ['اول', 'دوم', 'سوم', 'چهارم', 'پنجم']  
    buttons = []
    for idx, channel in enumerate(channels):
        text = f"کانال {persian_numbers[idx]}"
        buttons.append([InlineKeyboardButton(text=text, url=channel)])
    buttons.append([InlineKeyboardButton(text='عضو شدم',callback_data='join:joined')])
    return InlineKeyboardMarkup(buttons)


def plans_btn(plans , support_id=None ):
    buttoons = []
    for plan in plans :
        plan_tag = plan['tag']
        buttoons.append(InlineKeyboardButton(text=plan['name'], callback_data=f'plans:{plan_tag}'))
    chunked_buttons = [buttoons[i:i + 3] for i in range(0, len(buttoons), 3)]
    if  support_id : 
        chunked_buttons.append([InlineKeyboardButton(text='خرید اشتراک' , url=f'https://t.me/{support_id}')])
    return InlineKeyboardMarkup(chunked_buttons)

    
def get_file(call_data):
    buttons = [[InlineKeyboardButton(text='دریافت فایل',callback_data=call_data)]]
    return InlineKeyboardMarkup(buttons)



































































































