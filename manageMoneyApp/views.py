from rest_framework import viewsets
from rest_framework import permissions
from .serializers import currencieSerializer, usersBillSerializer, billCurrencieSerializer, userGoalSerializer,userHistorySerializer, userSettingSerializer
from .models import currencie, usersBill, billCurrencie, userGoal, userHistory, userSetting

class currencieViewSet(viewsets.ModelViewSet):
    queryset = currencie.objects.all()
    serializer_class = currencieSerializer
    permission_classes = [permissions.IsAuthenticated]

class usersBillViewSet(viewsets.ModelViewSet):
    queryset = usersBill.objects.all()
    serializer_class = usersBillSerializer
    permission_classes = [permissions.IsAuthenticated]

class billCurrencieViewSet(viewsets.ModelViewSet):
    queryset = billCurrencie.objects.all()
    serializer_class = billCurrencieSerializer
    permission_classes = [permissions.IsAuthenticated]

class userGoalViewSet(viewsets.ModelViewSet):
    queryset = userGoal.objects.all()
    serializer_class = userGoalSerializer
    permission_classes = [permissions.IsAuthenticated]

class userHistoryViewSet(viewsets.ModelViewSet):
    queryset = userHistory.objects.all()
    serializer_class = userHistorySerializer
    permission_classes = [permissions.IsAuthenticated]

class userSettingViewSet(viewsets.ModelViewSet):
    queryset = userSetting.objects.all()
    serializer_class = userSettingSerializer
    permission_classes = [permissions.IsAuthenticated]