from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from account.api.serializers import RegistrationSerializer
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
            #print(Account.objects.get(username=account).id)
            #token, created = Token.objects.get_or_create(user=account)
            #data['token'] = token.key
        else:
            data = serializer.errors
        return Response(data)
