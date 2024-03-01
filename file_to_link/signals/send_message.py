from django.db.models.signals import post_save
from django.dispatch import receiver
from file_to_link.models import SendMessageModel
from file_to_link.tasks import send_message_task



@receiver(post_save, sender=SendMessageModel)
def send_message_signal(sender, instance, created, **kwargs):
    if created :
        send_message_task.delay(instance.id)


