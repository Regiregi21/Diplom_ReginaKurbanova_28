import configuration
import requests

def create_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREAT_NEW_ORDERS,
                         json=body)

def get_order(track_number):
    get_order_url = f"{configuration.URL_SERVICE}/api/v1/orders/track?t={track_number}"
    return requests.get(get_order_url)