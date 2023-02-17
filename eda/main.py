import time
from brokers import EventBus 
from producers import produce, produce_post
from consumers import Consumer
from events import PostEvent

eventbus = EventBus()
eventbus.subscribe(PostEvent(), Consumer())

while eventbus.listen():
    time.sleep(10)