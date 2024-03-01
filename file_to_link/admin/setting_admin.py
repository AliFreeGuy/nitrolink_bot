from django.contrib import admin
from django.contrib import admin
from django.utils import timezone
from ..models import FileToLinkSettingModel

class FileToLinkSettingAdmin(admin.ModelAdmin):
    list_display = ( 'bot','is_active',)
    search_fields = ('bot__name',)
    list_filter = ('is_active',)
    ordering = ('-id',)
admin.site.register(FileToLinkSettingModel, FileToLinkSettingAdmin)
