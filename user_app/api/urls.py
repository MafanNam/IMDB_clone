from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path, include

from user_app.api import views

urlpatterns = [
    path('login/', obtain_auth_token, name='login'),
    path('register/', views.registration_view, name='register'),
    path('logout/', views.logout_view, name='logout'),

    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
