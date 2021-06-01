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

class userGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = userGoal
        fields = ['id','dateStart','dateEnd','description','goalSum']

class userHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = userHistory
        fields = ['id','date','operationID']

class userSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = userSetting
        fields = ['id','darkTheme','defaultCurrencie']