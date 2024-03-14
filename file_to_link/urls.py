from django.urls import path
from file_to_link.api import FileToLinkSettingApiView , FileToLinkPlansApiView  , UserUpdateAPIView , VolumeUsageAPIView

app_name = 'file_to_link'


urlpatterns = [
    path('api/setting/', FileToLinkSettingApiView.as_view() , name='setting'),
    path('api/plans/' ,FileToLinkPlansApiView.as_view() , name='plans' ),
    path('api/update_user/' , UserUpdateAPIView.as_view()  , name='update_user'),
    path('api/usage/' , VolumeUsageAPIView.as_view() , name='volume_usage')

    
]