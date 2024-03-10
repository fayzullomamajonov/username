from django.contrib import admin
from .models import (
    ProductModel, 
    RawMaterialModel,
    ProductMaterialModel,
    WarehousesModel,
    FactoryModel
    )

class WarehousesModelAdmin(admin.ModelAdmin):
    list_display = ('get_material_name', 'remainder', 'price','added_date')
    
    list_filter = ('added_date',)

    def get_material_name(self, obj):
        return obj.material.material
    
    get_material_name.short_description = 'Material Name'


class ProductMaterialModelAdmin(admin.ModelAdmin):
    list_display = ('get_product_name', 'get_raw_material_name','quantity',)

    def get_product_name(self, obj):
        return f"{obj.product.product_name} {obj.product.product_code}"
    
    get_product_name.short_description = 'Product Name'

    def get_raw_material_name(self, obj):
        return obj.raw_material.material
    
    get_raw_material_name.short_description = 'Raw Material Name'


admin.site.register(WarehousesModel,WarehousesModelAdmin)

admin.site.register(ProductModel)

admin.site.register(RawMaterialModel)

admin.site.register(ProductMaterialModel,ProductMaterialModelAdmin)

admin.site.register(FactoryModel)