from pyrogram import Client , filters
from utils import filters as f 
from config import BOT_TOKEN 
from utils.connection import connection as con
import math
from utils import text



INTERMEDIATE_ACCOUNT = 5512116521

@Client.on_message(
        filters.private &
        f.user_is_join &
        f.bot_is_active &
        f.user_is_active & (
        filters.document
        | filters.video
        | filters.audio
        | filters.voice
        | filters.photo
    ), group=3)

        

async def file_to_link_manager(client, msg):

    media = str(msg.media)

    if msg.from_user.id == msg.chat.id :
        if media == 'MessageMediaType.PHOTO' : 
                file_size = math.ceil(msg.photo.file_size  / (1024*1024))
                data = con.volume_usage(user=msg.from_user.id ,volume=int(file_size) , operation_type='increase' ,bot_status='file_to_link')
                
                if data  :
                        await msg.reply_text(text.loading_text, quote=True)
                        await client.send_photo(INTERMEDIATE_ACCOUNT , msg.photo.file_id , caption = f'{BOT_TOKEN}|{msg.from_user.id}|{str(int(msg.id) +1)}')
                
                elif data == False :
                        if msg.from_user.id == msg.chat.id :await msg.reply_text(text.user_not_volume , quote = True)
                else :
                        if msg.from_user.id == msg.chat.id :await msg.reply_text(text.somthing_error , quote = True)


        elif media == 'MessageMediaType.VIDEO': 
                file_size  = math.ceil(msg.video.file_size  / (1024*1024))
                data = con.volume_usage(user=msg.from_user.id ,volume=int(file_size) , operation_type='increase' ,bot_status='file_to_link')
                if data  :
                        await msg.reply_text(text.loading_text, quote=True)
                        await client.send_video(INTERMEDIATE_ACCOUNT , msg.video.file_id , caption = f'{BOT_TOKEN}|{msg.from_user.id}|{str(int(msg.id) +1)}')
                elif data == False :
                        if msg.from_user.id == msg.chat.id :await msg.reply_text(text.user_not_volume , quote = True)
                else :
                        if msg.from_user.id == msg.chat.id :await msg.reply_text(text.somthing_error , quote = True)

        elif media =='MessageMediaType.DOCUMENT': 
                file_size  = math.ceil(msg.document.file_size  / (1024*1024))
                data = con.volume_usage(user=msg.from_user.id ,volume=int(file_size) , operation_type='increase' ,bot_status='file_to_link')
                if data  :
                        await msg.reply_text(text.loading_text, quote=True)
                        await client.send_document(INTERMEDIATE_ACCOUNT , msg.document.file_id , caption = f'{BOT_TOKEN}|{msg.from_user.id}|{str(int(msg.id) +1)}')
                elif data == False :
                        if msg.from_user.id == msg.chat.id :await msg.reply_text(text.user_not_volume , quote = True)
                else :
                        if msg.from_user.id == msg.chat.id :await msg.reply_text(text.somthing_error , quote = True)

        # elif media == 'MessageMediaType.ANIMATION':
        #         file_size  = math.ceil(msg.animation.file_size  / (1024*1024))
        #         data = con.volume_usage(user=msg.from_user.id ,volume=int(file_size) , operation_type='increase' ,bot_status='file_to_link')
        #         if data  :
        #                 await msg.reply_text(text.loading_text, quote=True)
        #                 await client.send_animation(INTERMEDIATE_ACCOUNT , msg.animation.file_id , caption = f'{BOT_TOKEN}|{msg.from_user.id}|{str(int(msg.id) +1)}')
        #         elif data == False :
        #                 if msg.from_user.id == msg.chat.id :await msg.reply_text(text.user_not_volume , quote = True)
        #         else :
        #                 if msg.from_user.id == msg.chat.id :await msg.reply_text(text.somthing_error , quote = True)

        elif media == 'MessageMediaType.AUDIO'  :
                file_size  = math.ceil(msg.audio.file_size  / (1024*1024))
                data = con.volume_usage(user=msg.from_user.id ,volume=int(file_size) , operation_type='increase' ,bot_status='file_to_link')
                if data :
                        await msg.reply_text(text.loading_text, quote=True)
                        await client.send_audio(INTERMEDIATE_ACCOUNT , msg.audio.file_id , caption = f'{BOT_TOKEN}|{msg.from_user.id}|{str(int(msg.id) +1)}')
                elif data == False :
                        if msg.from_user.id == msg.chat.id :await msg.reply_text(text.user_not_volume , quote = True)
                else :
                        if msg.from_user.id == msg.chat.id :await msg.reply_text(text.somthing_error , quote = True)

        elif media == 'MessageMediaType.VOICE' : 
                file_size  = math.ceil(msg.voice.file_size  / (1024*1024))
                data = con.volume_usage(user=msg.from_user.id ,volume=int(file_size) , operation_type='increase' ,bot_status='file_to_link')
                if data  :
                        await msg.reply_text(text.loading_text, quote=True)
                        await client.send_voice(INTERMEDIATE_ACCOUNT , msg.voice.file_id , caption = f'{BOT_TOKEN}|{msg.from_user.id}|{str(int(msg.id) +1)}')
                elif data == False :
                        if msg.from_user.id == msg.chat.id :await msg.reply_text(text.user_not_volume , quote = True)
                else :
                        if msg.from_user.id == msg.chat.id :await msg.reply_text(text.somthing_error , quote = True)

        # elif media == 'MessageMediaType.STICKER' : 
        #         file_size  = math.ceil(msg.sticker.file_size  / (1024*1024))
        #         data = con.volume_usage(user=msg.from_user.id ,volume=int(file_size) , operation_type='increase' ,bot_status='file_to_link')
        #         if data  :
        #                 await msg.reply_text(text.loading_text, quote=True)
        #                 await client.send_sticker(INTERMEDIATE_ACCOUNT , msg.sticker.file_id , caption = f'{BOT_TOKEN}|{msg.from_user.id}|{str(int(msg.id) +1)}')
        #         elif data == False :
        #                 if msg.from_user.id == msg.chat.id :await msg.reply_text(text.user_not_volume , quote = True)
        #         else :
        #                 if msg.from_user.id == msg.chat.id :await msg.reply_text(text.somthing_error , quote = True)
