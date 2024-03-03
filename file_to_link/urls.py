from django.urls import path
from file_to_link.api import FileToLinkSettingApiView , FileToLinkPlansApiView

app_name = 'file_to_link'


urlpatterns = [
    path('api/setting/', FileToLinkSettingApiView.as_view() , name='setting'),
    path('api/plans/' ,FileToLinkPlansApiView.as_view() , name='plans' ),

    
]