from django.urls import path
from rest_framework import routers
from django.conf.urls import include
from api import views

app_name = 'api'

router = routers.DefaultRouter()
router.register('customers', views.CustomerViewSet)
router.register('carwashes', views.CarwashViewSet)
router.register('orders', views.OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
]