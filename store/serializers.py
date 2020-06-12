#serializers convert object data to another format 9here JSON)

from .models import Product 
from rest_framework import serializers 

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product #which model to serialize
        fields = "__all__" #what fields to serialize

