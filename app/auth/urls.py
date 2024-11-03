from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView
from .views import CustomTokenObtainPairView

urlpatterns = [

    path('login/', CustomTokenObtainPairView.as_view(), name='login_access'),
    path('login/refresh/', TokenRefreshView.as_view(), name='login_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='logout')

]