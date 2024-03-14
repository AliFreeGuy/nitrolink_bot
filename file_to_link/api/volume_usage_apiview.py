from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status  ,permissions  
from rest_framework.authentication import TokenAuthentication 
from file_to_link import forms
from file_to_link.models import UserFileToLinkModel , FileToLinkUsageModel , LinkToFileUsageModel
from accounts.models import User
from django.shortcuts import get_object_or_404

class VolumeUsageAPIView(APIView):
    authentication_classes = [TokenAuthentication,]
    permission_classes = [permissions.IsAuthenticated]
    
    def post(self, request):
        form = forms.VolumeUsageForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            main_user = get_object_or_404(User, chat_id=data['user'])
            user = get_object_or_404(UserFileToLinkModel, user=main_user)
            user_sub = main_user.user_filetolink.plans.filter(is_active=True).first()

            if user_sub:
                operation_type = data['operation_type']
                bot_status = data['bot_status']
                volume = data['volume']

                if bot_status == 'file_to_link':
                    if operation_type == 'increase':
                        try :
                            FileToLinkUsageModel.objects.create(user=user, usage=volume)
                        except Exception as e :
                            return Response({'error': f'Invalid volume {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
                    elif operation_type == 'decrease':
                        # Decrease logic if needed
                        pass

                elif bot_status == 'link_to_file':
                    if operation_type == 'increase':
                        try :
                            LinkToFileUsageModel.objects.create(user=user, usage=volume)
                        except Exception as e :
                            return Response({'error': f'Invalid volume {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

                    elif operation_type == 'decrease':
                        # Decrease logic if needed
                        pass

                return Response({'success': 'Volume usage updated successfully'}, status=status.HTTP_200_OK)
            else:
                return Response({'error': 'User does not have an active subscription'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'error': 'Invalid form'}, status=status.HTTP_400_BAD_REQUEST)
