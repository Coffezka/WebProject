from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from account.api.views import (
        registration_view,
        token_check
    )

app_name = "account"

urlpatterns = [
        path('register', registration_view, name="register"),
        path('login', obtain_auth_token, name="login"),
        path('tokencheck',token_check, name="tokenCheck"),
]