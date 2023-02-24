import time
import requests 
from producers import *
from events import PostEvent

res = requests.post('http://127.0.0.1:5001/short/subscribe', json={'event_type': "UserEvent", "subscriber": "/signup"})

produce_sign_up(_id="Test", name="Test", email="Test@gmail.com", password="test123", default_notification=None)

# res = requests.post('http://127.0.0.1:5001/short/listen')

# res = requests.post('http://127.0.0.1:5001/short/unsubscribe', json={'event_type': "PostEvent", "subscriber": "/post"})
