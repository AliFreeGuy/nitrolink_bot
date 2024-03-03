from django.db import models
from . import FileToLinkPlansModel ,UserFileToLinkModel
from core.models import BotModel
from django.utils import timezone
from datetime import timedelta


class UserPlanModel(models.Model):
    bot = models.ForeignKey(BotModel , on_delete = models.CASCADE , related_name = 'user_plans')
    user = models.ForeignKey(UserFileToLinkModel, on_delete=models.CASCADE, related_name='plans')
    plan = models.ForeignKey(FileToLinkPlansModel, on_delete=models.CASCADE, related_name='users')
    expiry = models.DateTimeField(null=True , blank=True)
    is_active = models.BooleanField(default = True)
    file_to_link_volume = models.PositiveBigIntegerField(default = 0)
    file_to_link_usage_to_day = models.PositiveBigIntegerField(default = 0)
    link_to_file_volume = models.PositiveBigIntegerField(default = 0)
    link_to_file_usage_to_day = models.PositiveBigIntegerField(default = 0)

    def __str__(self):
        return f'{self.user} - {self.plan}'
    
    def save(self, *args, **kwargs):
        if self.plan and self._state.adding:  # اگر نمونه جدید ایجاد شده باشد
            self.expiry = timezone.now() + timedelta(days=self.plan.day)
            self.file_to_link_volume = self.plan.file_to_link_volume
            self.link_to_file_volume = self.plan.link_to_file_volume
        super().save(*args, **kwargs)

class FileToLinkUsageModel(models.Model):
    user = models.ForeignKey(UserFileToLinkModel, on_delete=models.CASCADE, related_name='file_to_link_usage')
    date = models.DateField(auto_now_add=True)
    usage = models.BigIntegerField(default=0)

    def __str__(self):
        return f'{self.user.user} - {self.date} - File to Link Usage: {self.usage}'

class LinkToFileUsageModel(models.Model):
    user = models.ForeignKey(UserFileToLinkModel, on_delete=models.CASCADE, related_name='link_to_file_usage')
    date = models.DateField(auto_now_add=True)
    usage = models.BigIntegerField(default=0)

    def __str__(self):
        return f'{self.user.user} - {self.date} - Link to File Usage: {self.usage}'
