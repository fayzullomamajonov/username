from django.urls import path
from .views import ProductMaterialData


urlpatterns = [
    path("product_data/", ProductMaterialData.as_view()),
]
