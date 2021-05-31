from rest_framework import serializers
from .models import currencie, usersBill,userWant, userGoal, userHistory, userSetting

class currencieSerializer(serializers.ModelSerializer):
    class Meta:
        model = currencie
        fields = ['name','fullName','value']

class usersBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = usersBill
        fields = ['billName','img','currencieID','balance']

class usersWantSerializer(serializers.ModelSerializer):
    class Meta:
        model = userWant
        fields = ['name']

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