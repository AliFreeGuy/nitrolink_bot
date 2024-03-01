
from django.contrib import admin
from django.contrib import admin
from django.utils import timezone
from django.contrib import admin
from django.contrib import admin
from file_to_link.models import UserFileToLinkModel
from jdatetime import datetime


class FileToLinkUsersAdmin(admin.ModelAdmin):
    list_display = ('user', 'get_creation_jalali')
    search_fields = ('user__full_name__icontains', 'user__chat_id__icontains')
    ordering = ('-creation',)
    def get_creation_jalali(self, obj):
        return datetime.fromgregorian(datetime=obj.creation).strftime('%Y/%m/%d %H:%M:%S')
    get_creation_jalali.short_description = 'Creation '
admin.site.register(UserFileToLinkModel, FileToLinkUsersAdmin)
