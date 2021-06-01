import json
from rest_framework import status
from rest_framework.exceptions import ErrorDetail
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework.decorators import api_view

from account.api.serializers import RegistrationSerializer
from account.api.serializers import CheckTokenSerializer
from rest_framework.authtoken.models import Token
from account.models import Account
from manageMoneyApp.models import userSetting
from manageMoneyApp.models import currencie


@api_view(['POST',])
def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account = serializer.save()
            user_id = Account.objects.get(username=account)
            currencieObj = currencie.objects.get(name="UAH")
            user_setting = userSetting(userID = user_id, darkTheme= False, defaultCurrencie=currencieObj)
            user_setting.save()
            data['message'] = "registration was successful"
            #print(Account.objects.get(username=account).id)
            #token, created = Token.objects.get_or_create(user=account)
            #data['token'] = token.key
        else:
            data = serializer.errors
            print(serializer.errors)
        return Response(data)

@api_view(['POST',])
def token_check(request):
    if request.method == 'POST':
        serializer = CheckTokenSerializer(data=request.data)
        type = {'type':'error'}
        if serializer.is_valid():
            is_tokened = Token.objects.get(key=serializer.data["token"])
            if is_tokened :
                is_username = Account.objects.get(id=is_tokened.user_id).username == serializer.data["username"]
                if is_username:
                    type = {'type':'success'}
        return JsonResponse(type)
