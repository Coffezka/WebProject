
from django.contrib import admin
from django.urls import path
from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from rest_framework import renderers
from rest_framework.authtoken.views import obtain_auth_token
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
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/account/', include('account.api.urls', 'account_api'))
]
