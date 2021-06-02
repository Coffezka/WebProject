from drf_yasg.openapi import Operation
from rest_framework import serializers
from .models import currencie, userOperation, usersBill,userWant, userGoal, userHistory, userSetting

class currencieSerializer(serializers.ModelSerializer):
    class Meta:
        model = currencie
        fields = ['id','name','fullName','value']

class usersBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = usersBill
        fields = ['id','billName','img','currencieID','balance']

class usersWantSerializer(serializers.ModelSerializer):
    class Meta:
        model = userWant
        fields = ['id','name']

class usersOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = userOperation
        fields = ['id','type', 'sum','billID']

class usersOperationSerializerExtend(serializers.ModelSerializer):
    billID = usersBillSerializer(required=False)
    class Meta:
        model = userOperation
        fields = ['id','type', 'sum','billID']

class userGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = userGoal
        fields = ['id','dateStart','dateEnd','description','goalSum']

class userHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = userHistory
        fields = ['id','date','operationID']

class userHistorySerializerExtend(serializers.ModelSerializer):
    operationID = usersOperationSerializerExtend(required=False)
    class Meta:
        model = userHistory
        fields = ['id','date','operationID']

class userSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = userSetting
        fields = ['id','darkTheme','defaultCurrencie']

class userStatBind(serializers.Serializer):
   """Your data serializer, define your fields here."""
   date = serializers.CharField(max_length=1000)
   balance = serializers.CharField(max_length=1000)

# class userBillsBind(serializers.Serializer):
#    """Your data serializer, define your fields here."""
#    firstBillID = serializers.IntegerField()
#    secondBillID = serializers.IntegerField()
#    currencieID = serializers.IntegerField()