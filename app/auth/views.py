from django.utils import timezone
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView

from ..models import User

class CustomTokenObtainPairView(TokenObtainPairView): 

    def post(self, request, *args, **kwargs):

        try:
            response = super().post(request, *args, **kwargs)
        except Exception as e:
            return Response({
                'error' : str(e)
            })
        else:
            data = request.data
            user = User.objects.get(email=data.get("email")) # type: ignore
            user.last_login = timezone.now()
            user.save()
            return response
