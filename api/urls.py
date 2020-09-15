from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from api import views


router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet)

urlpatterns = [
    path('', include(router.urls)),
]