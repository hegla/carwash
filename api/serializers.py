from rest_framework import serializers
import main.models as models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ('id', 'name_surname', 'email', 'carwashes')


class CarwashSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Carwash
        fields = ('id', 'name', 'email', 'photo', 'website', 'location')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Order
        fields = '__all__'
