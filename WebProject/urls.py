
from django.contrib import admin
from django.urls import path
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework import renderers
from manageMoneyApp import views


router = routers.DefaultRouter()
router.register(r'userGoal-rest', views.userGoalViewSet)
router.register(r'userHistory-rest', views.userHistoryViewSet)
router.register(r'currencie-rest', views.currencieViewSet)
router.register(r'billCurrencie-rest', views.billCurrencieViewSet)
router.register(r'usersBill-rest', views.usersBillViewSet)
router.register(r'userSetting-rest', views.userSettingViewSet)



urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
