from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  ,permissions  
from rest_framework.authentication import TokenAuthentication 
from file_to_link.models import FileToLinkSettingModel
from ..serializers import FileToLinkSettingSerializer


class FileToLinkSettingApiView(APIView):
    authentication_classes = [TokenAuthentication ,]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, *args, **kwargs):
        setting = FileToLinkSettingModel.objects.first()
        if setting :
            ser_data = FileToLinkSettingSerializer(setting )
            return Response(ser_data.data , status=status.HTTP_200_OK)
        
        return Response({'data' : 'None'} , status=status.HTTP_404_NOT_FOUND)
    