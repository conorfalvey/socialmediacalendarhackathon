import time
import requests 
from producers import produce_post
from events import PostEvent

res = requests.post('http://127.0.0.1:5001/short/subscribe', json={'event_type': "PostEvent", "subscriber": "/post"})

res = requests.post('http://127.0.0.1:5001/short/subscribe', json={'event_type': "TestEvent", "subscriber": "/test"})


produce_post()
produce_post()

res = requests.post('http://127.0.0.1:5001/short/listen')

res = requests.post('http://127.0.0.1:5001/short/unsubscribe', json={'event_type': "PostEvent", "subscriber": "/post"})
