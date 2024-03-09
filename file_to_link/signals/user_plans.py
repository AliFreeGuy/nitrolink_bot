from django.db.models.signals import post_save
from django.dispatch import receiver
from file_to_link.models import UserPlanModel  , FileToLinkUsageModel , LinkToFileUsageModel
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime, timedelta
from django.core.exceptions import ValidationError


@receiver(post_save, sender=UserPlanModel)
def update_user_plans(sender, instance, created, **kwargs):
    if created:
        instance.user.plans.exclude(id=instance.id).update(is_active=False)


@receiver(post_save, sender=FileToLinkUsageModel)
def update_user_plan_file_to_link_usage(sender, instance, created, **kwargs):
    if created:
        user_plan = instance.user.plans.filter(is_active=True).first()
        if user_plan:
            today = datetime.now().date()
            files_downloaded_today = FileToLinkUsageModel.objects.filter(user=instance.user, date=today)
            total_usage_today = sum(file.usage for file in files_downloaded_today)

            if user_plan.plan.file_to_link_max_size == 0 or total_usage_today <= user_plan.plan.file_to_link_max_size:
                user_plan.file_to_link_volume = user_plan.file_to_link_volume - instance.usage
                user_plan.file_to_link_usage_to_day = total_usage_today
                user_plan.save()
            else:
                raise ValidationError("Your plan does not allow for this file-to-link usage.")
        else:
            raise ValidationError("No active plan found for this user.")


            
@receiver(post_save, sender=LinkToFileUsageModel)
def update_user_plan_link_to_file_usage(sender, instance, created, **kwargs):
    if created:
        user_plan = instance.user.plans.filter(is_active=True).first()
        if user_plan:
            today = datetime.now().date()
            files_downloaded_today = LinkToFileUsageModel.objects.filter(user=instance.user, date=today)
            total_usage_today = sum(file.usage for file in files_downloaded_today)
            
            if  user_plan.plan.link_to_file_max_size == 0 or total_usage_today <= user_plan.plan.link_to_file_max_size :
                user_plan.link_to_file_volume -= instance.usage
                user_plan.link_to_file_usage_to_day = total_usage_today
                user_plan.save()
            else:
                raise ValidationError("Your plan does not allow for this link_to_file usage.")
        else:
            raise ValidationError("No active plan found for this user.")

