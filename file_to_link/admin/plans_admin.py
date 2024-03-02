from django.contrib import admin
from file_to_link.models import FileToLinkPlansModel






class FileToLinkPlansAdmin(admin.ModelAdmin):
    list_display = ( 'tag', 'name', 'day', 'price', 'is_active')
    search_fields = ('bot__name', 'tag', 'name', 'day', 'volum', 'price')
    list_filter = ('bot', 'is_active')
    ordering = ('bot', 'name')
admin.site.register(FileToLinkPlansModel , FileToLinkPlansAdmin)
