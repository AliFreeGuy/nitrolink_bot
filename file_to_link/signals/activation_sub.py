
from django.db.models.signals import post_save , pre_save
from django.dispatch import receiver
from file_to_link.models import UserPlanModel , FileToLinkSettingModel
from file_to_link.tasks import send_quick_message

@receiver(post_save, sender=UserPlanModel)
def activation_user_sub_notification(sender, instance, created, **kwargs):
    if created:
        setting = FileToLinkSettingModel.objects.first()
        if setting :send_quick_message.delay(chat_id=instance.user.user.chat_id , message=setting.actication_sub_tex)
        else :send_quick_message.delay(chat_id=instance.user.user.chat_id , message='اشتراک شما فعال شد')
        