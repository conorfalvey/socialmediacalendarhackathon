import time
import requests 
from producers import *
from events import PostEvent

res = requests.post('http://127.0.0.1:5001/short/subscribe', json={'event_type': "UserEvent", "subscriber": "/signup"})

produce_sign_up(**{"ID":"Test", "Name":"Test", "Email":"Test@gmail.com", "Password":"test123", "Default_Notification":None})

res = requests.post('http://127.0.0.1:5001/short/listen')

# res = requests.post('http://127.0.0.1:5001/short/unsubscribe', json={'event_type': "PostEvent", "subscriber": "/post"})
