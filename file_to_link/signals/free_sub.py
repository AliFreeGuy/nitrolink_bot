
from django.db.models.signals import post_save , pre_save
from django.dispatch import receiver
from accounts.models import User
from file_to_link.models import UserFileToLinkModel , FileToLinkPlansModel , UserPlanModel
from core.models import BotModel







@receiver(post_save, sender=UserFileToLinkModel)
def add_free_sub_for_new_user(sender, instance, created, **kwargs):
    if created:
        free_sub = FileToLinkPlansModel.objects.filter(tag = 'free').first()
        print(free_sub)
        if free_sub :
            try :

                user = instance 
                bot = BotModel.objects.filter(name = 'file_to_link').first()
                data = UserPlanModel.objects.create(bot = bot , user = user , plan = free_sub)
                print('activation sub new user ')
            except Exception as e :
                print(f'ERROR: {str(e)}')