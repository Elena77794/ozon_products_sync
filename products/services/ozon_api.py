import requests
from django.http import JsonResponse
from django.conf import settings
from products.services.constants import OZON_API_URL, DEFAULT_LIMIT


def fetch_ozon_products():
    headers = {
        "Client-Id": settings.OZON_CLIENT_ID,
        "Api-Key": settings.OZON_API_KEY,
        "Content-Type": "application/json"

    }

    body = {
        "filter": {
            "visibility": "ALL"
        },

        "limit": DEFAULT_LIMIT
    }
    try:
        response = requests.post(OZON_API_URL, headers=headers, json=body)
        response.raise_for_status()
        data = response.json()

    except requests.exceptions.HTTPError as http_err:
        return JsonResponse({"error": f"HTTP error occurred: {http_err}"}, status=500)

    except requests.exceptions.RequestException as err:
        return JsonResponse({"error": f"Request error occurred: {err}"}, status=500)

    return JsonResponse(data)
