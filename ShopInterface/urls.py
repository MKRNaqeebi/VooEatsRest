"""

"""
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token,  verify_jwt_token

urlpatterns = [
    path('getToken/', obtain_jwt_token),
    path('tokenRefresh/', refresh_jwt_token),
    path('tokenVerify/', verify_jwt_token),
]
