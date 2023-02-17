import time
from brokers import EventBus 
from producers import produce, produce_post
from events import PostEvent

eventbus = EventBus()
eventbus.subscribe(PostEvent(), "/post")

while eventbus.listen():
    time.sleep(10)