from rest_framework import viewsets
from main import models
from api import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    permission_classes = (AllowAny,)


class CarwashViewSet(viewsets.ModelViewSet):
    queryset = models.Carwash.objects.all()
    serializer_class = serializers.CarwashSerializer
    permission_classes = (AllowAny,)


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = (AllowAny,)
