from django.contrib import admin
from django.urls import path
from products.views import products_list
urlpatterns = [
    path('admin/', admin.site.urls),
    path('products/', products_list)
]
