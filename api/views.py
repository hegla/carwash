from rest_framework import viewsets
from main import models
from api import serializers
from rest_framework.permissions import IsAuthenticated, AllowAny


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    permission_classes = (AllowAny,)
