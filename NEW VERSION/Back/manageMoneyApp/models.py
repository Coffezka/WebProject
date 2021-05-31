from django.db import models
from django.conf import settings




# Create your models here.

class currencie(models.Model):
    name = models.CharField(max_length=3) #Стандартом ISO 4217
    fullName = models.CharField(max_length=30)
    value = models.FloatField()

class usersBill(models.Model):
    userID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    billName = models.CharField(max_length=30)
    img = models.CharField(max_length=400)
    currencieID = models.ForeignKey(currencie, on_delete=models.CASCADE,null=True)
    balance = models.IntegerField(null=True)


class userGoal(models.Model):
    userID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    dateStart = models.DateTimeField()
    dateEnd = models.DateTimeField()
    description = models.CharField(max_length=500)
    goalSum = models.IntegerField()

class userWant(models.Model):
    userID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=500)

class userHistory(models.Model):
    userID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField()
    billID = models.ForeignKey(usersBill, on_delete=models.CASCADE)
    function = models.BooleanField() #function - дохід чи розхід
    category = models.IntegerField() #cat - в мене там іконка типу ставиться розхід на їжу, одяг і тд, аналогічно з доходом
    sum = models.IntegerField()
    currencieID = models.ForeignKey(currencie, on_delete=models.CASCADE)#FK

class userSetting(models.Model):
    userID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    darkTheme =  models.BooleanField()
    defaultCurrencie = models.ForeignKey(currencie, on_delete=models.CASCADE)


