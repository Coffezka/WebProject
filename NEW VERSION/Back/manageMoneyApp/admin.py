from django.contrib import admin
from .models import currencie
from .models import usersBill
from .models import usersStat
from .models import userOperation
from .models import userGoal
from .models import userWant
from .models import userHistory
from .models import userSetting

# Register your models here.
admin.site.register(currencie)
admin.site.register(userOperation)
admin.site.register(usersBill)
admin.site.register(usersStat)
admin.site.register(userWant)
admin.site.register(userGoal)
admin.site.register(userHistory)
admin.site.register(userSetting)
