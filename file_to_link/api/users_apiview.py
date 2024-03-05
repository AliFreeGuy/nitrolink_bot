from rest_framework.views import APIView
from rest_framework.response import Response 
from accounts.models import User
from file_to_link.models import UserFileToLinkModel
from rest_framework.authentication import TokenAuthentication
from rest_framework import status  ,permissions
from rest_framework.serializers import ValidationError
from django.http import HttpResponse
from file_to_link.serializers import UserSerializer



class UserUpdateAPIView(APIView):
    authentication_classes = [TokenAuthentication, ]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
    
        try:
            user = User.objects.filter(chat_id=request.data.get('chat_id'))

            if not user.exists():
                data = request.data
                new_user, created = User.objects.get_or_create(chat_id=data.get('chat_id'), full_name=data.get('full_name'))
                UserFileToLinkModel(user=new_user).save()
                return Response(UserSerializer(new_user).data, status=status.HTTP_200_OK)
            
            user = user.first()
            
            if request.data.get('full_name'):
                user.full_name = request.data.get('full_name')
                user.save()
            return Response(UserSerializer(user).data, status=status.HTTP_200_OK)

        except ValidationError as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)