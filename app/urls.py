from django.urls import include, path

urlpatterns = [
    path('user/', include('app.user.urls')),
    path('auth/', include('app.auth.urls')),
]