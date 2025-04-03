from django.http import JsonResponse
import requests
from products.services.ozon_api import fetch_ozon_products


def get_ozon_products(request):
    data = fetch_ozon_products()
    return data
