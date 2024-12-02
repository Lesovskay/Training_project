import configuration
import requests
import data

def post_new_order(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_ORDER,
                         json=body)

def get_track():
    order = post_new_order(data.order_body)
    return order.json().get("track")

def get_order_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + str(track))

