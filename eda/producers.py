from events import NotificationEvent, PostEvent
import requests

def produce_post():
    event = PostEvent(id="Test", platform="Test", delivery_time="Test", text="Test", frequency="Test", user_id="Test")
    res = requests.post('http://127.0.0.1:5001/short/add', json=event.to_repr())


def produce_notificaiton():
    event = NotificationEvent(email="Test")
    res = requests.post('http://127.0.0.1:5001/short/add')