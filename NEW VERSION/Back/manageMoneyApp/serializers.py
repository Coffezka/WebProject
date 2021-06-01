from rest_framework import serializers
from .models import currencie, userOperation, usersBill,userWant, userGoal, userHistory, userSetting

class currencieSerializer(serializers.ModelSerializer):
    class Meta:
        model = currencie
        fields = ['id','name','fullName','value']

class usersBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = usersBill
        fields = ['billName','img','currencieID','balance']

class usersWantSerializer(serializers.ModelSerializer):
    class Meta:
        model = userWant
        fields = ['name']

class usersOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = userOperation
        fields = ['type', 'sum']

class userGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = userGoal
        fields = ['dateStart','dateEnd','description','goalSum']

class userHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = userHistory
        fields = ['date','billID','function','category','sum','currencieID']

class userSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = userSetting
        fields = ['darkTheme','defaultCurrencie']