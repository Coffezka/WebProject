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

class usersStat(models.Model):
    userID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    date = models.TextField(max_length=1000)
    balance = models.TextField(max_length=1000)


class userGoal(models.Model):
    userID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    dateStart = models.CharField(max_length=500)
    dateEnd = models.CharField(max_length=500)
    description = models.CharField(max_length=500)
    goalSum = models.IntegerField()

class userOperation(models.Model):
    userID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    type = models.BooleanField()
    sum = models.IntegerField()
    billID = models.ForeignKey(usersBill, on_delete=models.CASCADE,null=True)

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
    date = models.CharField(max_length=500)
    operationID = models.ForeignKey(userOperation, on_delete=models.CASCADE,null=True)

class userSetting(models.Model):
    userID = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    darkTheme =  models.BooleanField()
    defaultCurrencie = models.ForeignKey(currencie, on_delete=models.CASCADE)


