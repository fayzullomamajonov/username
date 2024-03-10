from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from .models import FactoryModel, ProductMaterialModel, WarehousesModel, ProductModel, RawMaterialModel

class ProductMaterialDataTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.product = ProductModel.objects.create(product_name="Product 1", product_code=1)
        self.raw_material = RawMaterialModel.objects.create(material="Raw Material 1")
        self.warehouse = WarehousesModel.objects.create(material=self.raw_material, remainder=100, price=10)
        self.factory = FactoryModel.objects.create(product=self.product, product_count=10)
        self.product_material = ProductMaterialModel.objects.create(product=self.product, raw_material=self.raw_material, quantity=2)

    def test_product_material_data_view(self):
        url = reverse('product-material-data')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(response.data['result']), 1)  

        self.assertEqual(response.data['result'][0]['product_name'], 'Product 1')

