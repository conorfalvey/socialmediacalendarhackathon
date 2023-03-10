from events import *
import requests

def produce_post():
    event = PostEvent(id="Test", platform="Test", delivery_time="Test", text="Test", frequency="Test", user_id="Test")
    res = requests.post('http://127.0.0.1:5001/short/add', json=event.to_repr())


def produce_notification():
    event = NotificationEvent(email="Test")
    res = requests.post('http://127.0.0.1:5001/short/add', json=event.to_repr())

def produce_sign_up(**kwargs):
    event = UserEvent(**kwargs)
    print(event.to_repr())
    res = requests.post('http://127.0.0.1:5001/short/add', json=event.to_repr())