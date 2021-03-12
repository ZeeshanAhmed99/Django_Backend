from django.urls import include,path
from rest_framework import routers
from .import views

router = routers.DefaultRouter()
router.register(r'getEmail',views.getdataViewSet)
urlpatterns = [
    path('', views.index, name='index'),
    path('form',views.data,name='data'),
    path('login',views.login,name='login'),
    path('temp',views.temp,name='temp'),
    path('data',views.database,name='database'),
    path('removepunc',views.removepunc,name = 'removepunc'),
    path('capital',views.capital,name = 'capital'),
    path('', include(router.urls)),
   # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]