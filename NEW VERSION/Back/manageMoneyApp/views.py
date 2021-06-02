import datetime
from rest_framework import viewsets
from rest_framework import authentication,permissions
from .serializers import currencieSerializer, usersOperationSerializer, usersWantSerializer, usersBillSerializer, userGoalSerializer,userHistorySerializer, userSettingSerializer, userBillsBind
from .models import currencie, usersBill, userOperation, userWant, userGoal, userHistory, userSetting
from rest_framework.authtoken.models import Token
from rest_framework import filters
from rest_framework.response import Response
from rest_framework import mixins
from django.http import JsonResponse
from rest_framework.decorators import api_view

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
    search_fields = ['billName']

    def perform_create(self, serializer):
        return serializer.save(userID=self.request.user)
    def perform_update(self, serializer):
        return serializer.save(userID=self.request.user)

class usersOperationViewSet(mixins.RetrieveModelMixin,mixins.CreateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = userOperation.objects.all()
    serializer_class = usersOperationSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def perform_create(self, serializer):
        operation = serializer.save(userID=self.request.user)  
        user_history = userHistory(userID = self.request.user,date = int(round(datetime.datetime.now().timestamp() * 1000)),operationID = operation)
        user_history.save()
    def perform_update(self, serializer):
        return serializer.save(userID=self.request.user)


class userWantViewSet(viewsets.ModelViewSet):
    filter_backends = (OwnerFilterBackend,filters.SearchFilter,)
    queryset = userWant.objects.all()
    serializer_class = usersWantSerializer
    authentication_classes = [authentication.TokenAuthentication]
    search_fields = ['name']

    def perform_create(self, serializer):
        return serializer.save(userID=self.request.user)
    def perform_update(self, serializer):
        return serializer.save(userID=self.request.user)

class userGoalViewSet(viewsets.ModelViewSet):
    filter_backends = (OwnerFilterBackend,filters.SearchFilter,)
    queryset = userGoal.objects.all()
    serializer_class = userGoalSerializer
    authentication_classes = [authentication.TokenAuthentication]
    
    search_fields = ['description']

    def perform_create(self, serializer):
        return serializer.save(userID=self.request.user)
    def perform_update(self, serializer):
        return serializer.save(userID=self.request.user)


class userHistoryViewSet(viewsets.ModelViewSet):
    filter_backends = (OwnerFilterBackend,filters.SearchFilter,)
    queryset = userHistory.objects.all()
    serializer_class = userHistorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    search_fields = ['function','date']

    def perform_create(self, serializer):
        return serializer.save(userID=self.request.user)
    def perform_update(self, serializer):
        return serializer.save(userID=self.request.user)


class userSettingViewSet(mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    filter_backends = (OwnerFilterBackend,)
    queryset = userSetting.objects.all()
    serializer_class = userSettingSerializer
    authentication_classes = [authentication.TokenAuthentication]
    
    def perform_create(self, serializer):
        return serializer.save(userID=self.request.user)
    def perform_update(self, serializer):
        return serializer.save(userID=self.request.user)

@api_view(['POST',])
def userBillBind(request):
    if request.method == 'POST':
        serializer = userBillsBind(data=request.data)
        
        if serializer.is_valid():

            return JsonResponse({'type':serializer.data['firstBillID']})
        return JsonResponse({'type':'ErrorBind'})
    

