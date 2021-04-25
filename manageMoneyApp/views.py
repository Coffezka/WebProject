from rest_framework import viewsets
from rest_framework import authentication,permissions
from .serializers import currencieSerializer, usersBillSerializer, billCurrencieSerializer, userGoalSerializer,userHistorySerializer, userSettingSerializer
from .models import currencie, usersBill, billCurrencie, userGoal, userHistory, userSetting
from rest_framework.response import Response

class currencieViewSet(viewsets.ModelViewSet):
    queryset = currencie.objects.all()
    serializer_class = currencieSerializer


class usersBillViewSet(viewsets.ModelViewSet):
    queryset = usersBill.objects.all()
    serializer_class = usersBillSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class billCurrencieViewSet(viewsets.ModelViewSet):
    queryset = billCurrencie.objects.all()
    serializer_class = billCurrencieSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class userGoalViewSet(viewsets.ModelViewSet):
    queryset = userGoal.objects.all()
    serializer_class = userGoalSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]


class userHistoryViewSet(viewsets.ModelViewSet):
    queryset = userHistory.objects.all()
    serializer_class = userHistorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class userSettingViewSet(viewsets.ModelViewSet):
    queryset = userSetting.objects.all()
    serializer_class = userSettingSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]