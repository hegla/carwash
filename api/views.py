from rest_framework import viewsets
from main import models
from api import serializers
from rest_framework.permissions import BasePermission, IsAuthenticated, AllowAny, IsAdminUser, SAFE_METHODS
from allauth.socialaccount.providers.facebook.views import FacebookOAuth2Adapter
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from rest_auth.registration.views import SocialLoginView


class ReadOnly(BasePermission):
    def has_permission(self, request, view):
        print(request.method)
        return request.method in SAFE_METHODS


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = models.Customer.objects.all()
    serializer_class = serializers.CustomerSerializer
    permission_classes = (IsAdminUser,)


class CarwashViewSet(viewsets.ModelViewSet):
    queryset = models.Carwash.objects.all()
    serializer_class = serializers.CarwashSerializer
    permission_classes = [IsAdminUser|ReadOnly]


class OrderViewSet(viewsets.ModelViewSet):
    queryset = models.Order.objects.all()
    serializer_class = serializers.OrderSerializer
    permission_classes = [IsAdminUser|ReadOnly]


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    callback_url = '/'