from django.urls import path, include
from .views import UserProfileView

app_name = 'users'

urlpatterns = [
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    path('<username>/<id>/', UserProfileView.as_view(), name='profile'),
]
