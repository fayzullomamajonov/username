from .models import ProductModel,FactoryModel
from rest_framework import serializers


class ProductModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductModel
        fields = "__all__"


class FactoryModelSerializer(serializers.ModelSerializer):
    product_name = serializers.SerializerMethodField()
    class Meta:
        model = FactoryModel
        fields = ('product_name','product_count',)
    
    def get_product_name(self, obj):
        return f"{obj.product.product_name}-{obj.product.product_code}" if obj.product else None
