from rest_framework import serializers
from .models import currencie, usersBill, billCurrencie, userGoal, userHistory, userSetting

class currencieSerializer(serializers.ModelSerializer):
    class Meta:
        model = currencie
        fields = ['name','fullName','value']

class usersBillSerializer(serializers.ModelSerializer):
    class Meta:
        model = usersBill
        fields = ['userID','billName','img']

class billCurrencieSerializer(serializers.ModelSerializer):
    class Meta:
        model = billCurrencie
        fields = ['billID','currencieID','balance']

class userGoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = userGoal
        fields = ['userID','dateStart','dateEnd','description','goalSum']

class userHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = userHistory
        fields = ['userID','date','billID','function','category','sum','currencieID']

class userSettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = userSetting
        fields = ['userID','darkTheme','defaultCurrencie']