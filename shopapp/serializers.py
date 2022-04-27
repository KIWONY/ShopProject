from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.authtoken import models

from shopapp.models import Product


class ProductSerializer(serializers.ModelSerializer):

    products = serializers.StringRelatedField(many=True)

    class Meta:
        model = Product

        fields = ["products", "price" , "available_order"]
