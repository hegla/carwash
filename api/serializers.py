from rest_framework import serializers
import main.models as models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ('id', 'name', 'surname', 'email', 'carwashes')


class CarwashSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carwash
        fields = ('id', 'email', 'photo', 'website')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'
