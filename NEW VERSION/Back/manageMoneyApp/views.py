import datetime
import time
from rest_framework import viewsets
from rest_framework import authentication,permissions
from .serializers import currencieSerializer, usersOperationSerializerExtend, userHistorySerializerExtend,usersOperationSerializer, usersWantSerializer, usersBillSerializer, userGoalSerializer,userHistorySerializer, userSettingSerializer
from .models import currencie, usersStat, usersBill, userOperation, userWant, userGoal, userHistory, userSetting
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
    #serializer_class = usersOperationSerializer
    authentication_classes = [authentication.TokenAuthentication]

    def perform_create(self, serializer):
        operation = serializer.save(userID=self.request.user)
        bill_id = getattr(operation,"billID").id
        user_bill = usersBill.objects.get(pk = bill_id)
        if getattr(operation,"type") ==  True:
            user_bill.balance += getattr(operation,"sum") 
        else:
            user_bill.balance -= getattr(operation,"sum") 
        user_bill.save()
        if usersStat.objects.filter(userID = self.request.user).count() == 0:
            stat = usersStat(userID = self.request.user)
            stat.date = stat.date + str(round(time.time() * 1000)) + " "
            stat.balance = str(getattr(operation,"sum")) + " "
            stat.save()
        else:
            bills = usersBill.objects.filter(userID=self.request.user)
            balance = 0
            for i, c in enumerate(bills):
                num = getattr(c, "balance")
                cof = getattr(getattr(c, "currencieID"), "value")
                balance += (num*cof)
            stat = usersStat.objects.get(userID = self.request.user)
            stat.date = stat.date + str(round(time.time() * 1000)) + " "
            stat.balance = stat.balance + str(round(balance)) + " "
            stat.save()
        
        user_history = userHistory(userID = self.request.user,date = int(round(datetime.datetime.now().timestamp() * 1000)),operationID = operation)
        user_history.save()
    def perform_update(self, serializer):
        return serializer.save(userID=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return usersOperationSerializerExtend
        if self.action == 'retrieve':
            return usersOperationSerializerExtend
        return usersOperationSerializer

class userStatViewSet(viewsets.ModelViewSet):
    queryset = usersStat.objects.all()
    serializer_class = usersWantSerializer
    authentication_classes = [authentication.TokenAuthentication]
    search_fields = ['name']

    def perform_create(self, serializer):
        return serializer.save(userID=self.request.user)
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
    #serializer_class = userHistorySerializer
    authentication_classes = [authentication.TokenAuthentication]
    search_fields = ['function','date']

    def perform_create(self, serializer):
        return serializer.save(userID=self.request.user)
    def perform_update(self, serializer):
        return serializer.save(userID=self.request.user)

    def get_serializer_class(self):
        if self.action == 'list':
            return userHistorySerializerExtend
        if self.action == 'retrieve':
            return userHistorySerializerExtend
        return userHistorySerializer


class userSettingViewSet(mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.UpdateModelMixin,viewsets.GenericViewSet):
    filter_backends = (OwnerFilterBackend,)
    queryset = userSetting.objects.all()
    serializer_class = userSettingSerializer
    authentication_classes = [authentication.TokenAuthentication]
    
    def perform_create(self, serializer):
        return serializer.save(userID=self.request.user)
    def perform_update(self, serializer):
        return serializer.save(userID=self.request.user)

@api_view(['GET',])
def userStatat(request):
    if usersStat.objects.filter(userID=request.user).count() == 0:
        return JsonResponse({"message": "your bill is empty"})
    else:
        balance = usersStat.objects.get(userID=request.user)
        return JsonResponse({ "message": "success", "date" :  getattr(balance,"date"), "balance": getattr(balance,"balance")})
    

@api_view(['GET',])
def userBalance(request):
    bills = usersBill.objects.filter(userID=request.user)
    balance = 0
    for i, c in enumerate(bills):
        num = getattr(c, "balance")
        cof = getattr(getattr(c, "currencieID"), "value")
        balance += (num*cof)
        
    return JsonResponse({'Balance': balance})
    

