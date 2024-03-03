from file_to_link.models import FileToLinkSettingModel
from rest_framework import serializers
from file_to_link.models import FileToLinkPlansModel

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
