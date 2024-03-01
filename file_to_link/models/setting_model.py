from django.db import models
from core.models import BotModel



class FileToLinkSettingModel(models.Model):
    bot = models.OneToOneField(BotModel , on_delete = models.CASCADE , related_name = 'setting')
    is_active = models.BooleanField(default = True )
    not_active_text = models.TextField(default = 'خالی')
   
    support_id = models.CharField(max_length = 128 ,default = 'خالی' )
    support_text= models.TextField(default = 'خالی')
    help_text = models.TextField(default = 'خالی' )
    start_text = models.TextField(default = 'خالی' )
    user_not_active_text = models.TextField(default = 'خالی')
    join_channel_text = models.TextField(default = 'خالی')


    file_to_link_status = models.BooleanField(default = True )
    file_to_link_off_text = models.TextField(default = 'خالی')

    link_to_file_status = models.BooleanField(default = True)
    link_to_file_off_text = models.TextField(default = 'خالی' )


    channel_1  = models.CharField(max_length = 248 , null = True , blank = True)
    channel_2  = models.CharField(max_length = 248 , null = True , blank = True)
    channel_3  = models.CharField(max_length = 248 , null = True , blank = True)
    channel_4 = models.CharField(max_length = 248 , null = True , blank = True)
    channel_5  = models.CharField(max_length = 248 , null = True , blank = True)

    def __str__(self) -> str:
        return 'FileToLink Setting'
    

    class Meta :
        verbose_name = "FileToLink Setting"
        verbose_name_plural = "FileToLink Setting"