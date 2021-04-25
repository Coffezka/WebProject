from django.db import models

# Create your models here.

class currencie(models.Model):
    name = models.CharField(max_length=3) #Стандартом ISO 4217
    fullName = models.CharField(max_length=30)
    value = models.IntegerField()

class usersBill(models.Model):
    userID = models.CharField(max_length=400) #FK
    billName = models.CharField(max_length=30)
    img = models.CharField(max_length=400)

class billCurrencie(models.Model):
    billID = models.ForeignKey(usersBill, on_delete=models.CASCADE)
    currencieID = models.ForeignKey(currencie, on_delete=models.CASCADE)
    balance = models.IntegerField()

class userGoal(models.Model):
    userID = models.CharField(max_length=400) #FK
    dateStart = models.DateTimeField()
    dateEnd = models.DateTimeField()
    description = models.CharField(max_length=500)
    goalSum = models.IntegerField()

class userHistory(models.Model):
    userID = models.CharField(max_length=400) #FK
    date = models.DateTimeField()
    billID = models.ForeignKey(usersBill, on_delete=models.CASCADE)
    function = models.BooleanField() #function - дохід чи розхід
    category = models.IntegerField() #cat - в мене там іконка типу ставиться розхід на їжу, одяг і тд, аналогічно з доходом
    sum = models.IntegerField()
    currencieID = models.ForeignKey(currencie, on_delete=models.CASCADE)#FK

class userSetting(models.Model):
    userID = models.CharField(max_length=400)#FK
    darkTheme =  models.BooleanField()
    defaultCurrencie = models.ForeignKey(currencie, on_delete=models.CASCADE)


