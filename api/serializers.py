from rest_framework import serializers
import main.models as models

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Customer
        fields = ('id', 'name', 'surname', 'email', 'carwashes')
        