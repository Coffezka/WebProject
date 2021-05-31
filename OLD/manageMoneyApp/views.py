from rest_framework import viewsets
from rest_framework import authentication,permissions
from .serializers import currencieSerializer, usersBillSerializer, userGoalSerializer,userHistorySerializer, userSettingSerializer
from .models import currencie, usersBill, userGoal, userHistory, userSetting
from rest_framework.authtoken.models import Token
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins

class OwnerFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request, queryset, view):
        return queryset.filter(userID=request.user)


class currencieViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = currencie.objects.all()
    serializer_class = currencieSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'fullName']


class usersBillViewSet(viewsets.ModelViewSet):
    filter_backends = (OwnerFilterBackend,filters.SearchFilter,)
    queryset = usersBill.objects.all()
    serializer_class = usersBillSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['billName']

class userGoalViewSet(viewsets.ModelViewSet):
    filter_backends = (OwnerFilterBackend,filters.SearchFilter,)
    queryset = userGoal.objects.all()
    serializer_class = userGoalSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['description']
    
    


class userHistoryViewSet(viewsets.ReadOnlyModelViewSet):
    filter_backends = (OwnerFilterBackend,filters.SearchFilter,)
    queryset = userHistory.objects.all()
    serializer_class = userHistorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    search_fields = ['function','date']

class userSettingViewSet(mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    filter_backends = (OwnerFilterBackend,)
    queryset = userSetting.objects.all()
    serializer_class = userSettingSerializer
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

