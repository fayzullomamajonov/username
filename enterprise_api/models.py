from django.db import models
import uuid
# Create your models here.

class ProductModel(models.Model):
    product_name = models.CharField(max_length=25)
    product_code = models.IntegerField(primary_key=True)


    def __str__(self):
        return f"{self.product_name} {self.product_code}"
    
class RawMaterialModel(models.Model):
    material = models.CharField(max_length=50)

    def __str__(self):
        return self.material
    
class ProductMaterialModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete = models.DO_NOTHING, related_name='product')
    raw_material = models.ForeignKey(RawMaterialModel,on_delete = models.DO_NOTHING, related_name='raw_material')
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.raw_material.material}"


class WarehousesModel(models.Model):
    material = models.ForeignKey(RawMaterialModel,on_delete = models.DO_NOTHING, related_name='warehouses')
    remainder = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    added_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.material.material}"
    


class FactoryModel(models.Model):
    product = models.ForeignKey(ProductModel, on_delete=models.DO_NOTHING, related_name='factory_products')
    product_count = models.IntegerField()

    def __str__(self):
        return f"{self.product.product_name} {self.product_count}"