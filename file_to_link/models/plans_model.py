from django.db import models
from core.models import BotModel



class FileToLinkPlansModel(models.Model):
    bot = models.ForeignKey(BotModel , on_delete = models.CASCADE , related_name = 'plans')
    tag = models.CharField(max_length = 128 , unique = True )   
    name = models.CharField(max_length = 128 ,  unique = True)
    day = models.BigIntegerField()
    file_to_link_volume = models.BigIntegerField()
    file_to_link_max_size = models.BigIntegerField()
    link_to_file_volume = models.BigIntegerField()
    link_to_file_max_size = models.BigIntegerField()
    des = models.TextField(verbose_name = 'description' , default = 'خالی')
    price = models.BigIntegerField()
    is_active = models.BooleanField(default = True)


    def __str__(self) -> str:
        return str(self.name)


    class Meta :
        verbose_name =  'Plans'
        verbose_name_plural = 'Plans'
