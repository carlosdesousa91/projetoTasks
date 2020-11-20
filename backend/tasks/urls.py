from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from rest_framework.authtoken.views import obtain_auth_token
from tasks.fazer.views import FazerViewSet
from rest_framework import routers
from crudtasks import views


router =routers.DefaultRouter()
router.register(r'fazer', FazerViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('auth/', obtain_auth_token),
    path('tas', views.tas),
    
]
