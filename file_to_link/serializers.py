from file_to_link.models import FileToLinkSettingModel
from rest_framework import serializers
from file_to_link.models import FileToLinkPlansModel
from accounts.models import User
from file_to_link.models import UserPlanModel


class FileToLinkSettingSerializer(serializers.ModelSerializer):
    channels = serializers.SerializerMethodField()

    def get_channels(self, obj):
        channels = [obj.channel_1, obj.channel_2, obj.channel_3, obj.channel_4, obj.channel_5]
        channels = [channel for channel in channels if channel]
        return channels

    class Meta:
        model = FileToLinkSettingModel
        fields = '__all__'



class FileToLinkPlansSerializers(serializers.ModelSerializer):
    class Meta :
        model = FileToLinkPlansModel
        fields = '__all__'


class UserSubServializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlanModel
        fields = '__all__'




class UserSerializer(serializers.ModelSerializer):
    sub = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = '__all__'

    def get_sub(self, obj):
        user_subs = obj.user_filetolink.plans.filter(is_active = True).first()
        serializer = UserSubServializer(user_subs)
        return serializer.data