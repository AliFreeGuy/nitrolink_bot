from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication
from rest_framework import status , permissions
from file_to_link.serializers import FileToLinkPlansSerializers
from file_to_link.models import FileToLinkPlansModel



class FileToLinkPlansApiView(APIView):
    authentication_classes = [TokenAuthentication ,]
    permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
    

    def get(self , request ):
        plans = FileToLinkPlansModel.objects.filter(is_active = True)
        ser_data = FileToLinkPlansSerializers(plans , many = True)
        return Response(ser_data.data)
