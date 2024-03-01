from django.contrib import admin
from core.models import BotModel

from django.contrib import admin
from core.models import BotModel

class BotModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'token')
    search_fields = ('name', 'username', 'token')
    ordering = ('name',)

admin.site.register(BotModel, BotModelAdmin)


