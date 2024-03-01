from django.contrib import admin
from file_to_link.models import SendMessageModel




class SendMessageModelAdmin(admin.ModelAdmin):
    list_display = ('message', 'creation')
    filter_horizontal = ('user',)
    search_fields = ('message',)
    ordering = ('-creation',)
admin.site.register(SendMessageModel, SendMessageModelAdmin)

