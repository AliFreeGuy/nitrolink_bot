from .setting_admin import FileToLinkSettingAdmin
from .users_admin import FileToLinkUsersAdmin
from .send_message_admin import SendMessageModelAdmin
from .plans_admin import FileToLinkPlansAdmin



from file_to_link.models import UserPlanModel , FileToLinkUsageModel , LinkToFileUsageModel
from django.contrib import admin



admin.site.register(UserPlanModel )
admin.site.register(FileToLinkUsageModel )
admin.site.register(LinkToFileUsageModel )
