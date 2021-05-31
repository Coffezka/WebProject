
from django.contrib import admin
from django.urls import path
from django.urls import path
from django.conf.urls import include
from django.conf.urls import url
from rest_framework import routers
from rest_framework import renderers
from rest_framework.authtoken.views import obtain_auth_token
from manageMoneyApp import views

#swagger
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Snippets API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)



router = routers.DefaultRouter()
router.register(r'userGoal-rest', views.userGoalViewSet)
router.register(r'userHistory-rest', views.userHistoryViewSet)
router.register(r'userWant-rest', views.userWantViewSet)
router.register(r'currencie-rest', views.currencieViewSet)
router.register(r'usersBill-rest', views.usersBillViewSet)
router.register(r'userSetting-rest', views.userSettingViewSet)



urlpatterns = [
    url(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    url(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    url(r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    #path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    path('api/account/', include('account.api.urls', 'account_api'))
]
