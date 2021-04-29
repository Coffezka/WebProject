from rest_framework import viewsets
from rest_framework import authentication,permissions
from .serializers import currencieSerializer, usersBillSerializer, billCurrencieSerializer, userGoalSerializer,userHistorySerializer, userSettingSerializer
from .models import currencie, usersBill, billCurrencie, userGoal, userHistory, userSetting
from rest_framework.authtoken.models import Token
from rest_framework import filters

class OwnerFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(userID=request.user)

class currencieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = currencie.objects.all()
    serializer_class = currencieSerializer


class usersBillViewSet(viewsets.ModelViewSet):
    filter_backends = (OwnerFilterBackend,)
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
    filter_backends = (OwnerFilterBackend,)
    queryset = userGoal.objects.all()
    serializer_class = userGoalSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    


class userHistoryViewSet(viewsets.ModelViewSet):
    filter_backends = (OwnerFilterBackend,)
    queryset = userHistory.objects.all()
    serializer_class = userHistorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

class userSettingViewSet(viewsets.ModelViewSet):
    filter_backends = (OwnerFilterBackend,)
    queryset = userSetting.objects.all()
    serializer_class = userSettingSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]