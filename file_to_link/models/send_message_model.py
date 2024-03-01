from django.db import models
from file_to_link.models import UserFileToLinkModel


class SendMessageModel(models.Model):
    user = models.ManyToManyField(UserFileToLinkModel, related_name='admin_message')
    message = models.TextField()
    creation = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return str(self.message[:30])

    
    class Meta :

        verbose_name = "SendMessage"
        verbose_name_plural = "SendMessage"