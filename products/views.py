from django.http import  JsonResponse
import requests
from django.conf import settings

token = settings.OZON_API_KEY

def products_list(request):
    url = "https://api-seller.ozon.ru/v3/product/list"
    headers = {
        "Client-Id": "1818",
        "Api-Key": token,
        "Content-Type": "application/json"

    }

    body = {
        "filter": {
            "visibility": "ALL"
        },

        "limit": 10
    }
    try:
        response = requests.post(url, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()
    except requests.exceptions.RequestException as e:
        return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse(data)