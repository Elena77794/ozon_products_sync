from django.contrib import admin
from django.urls import path
from products.views import get_ozon_products
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', get_ozon_products, name="ozon_products")
]
