from django.http import JsonResponse
import requests
from products.services.ozon_api import fetch_ozon_products
from django.shortcuts import render


def get_ozon_products(request):
    data = fetch_ozon_products()
    items = data.get("result", {}).get("items", [])
    return render(request, "products/ozon_products.html", {"products": items})
