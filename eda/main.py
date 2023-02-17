import time
from brokers import EventBus 
from producers import produce, produce_post
from events import PostEvent

eventbus = EventBus()
eventbus.subscribe(PostEvent(bypass=True), "/post")

produce_post(eventbus)
while eventbus.listen():
    print("Done")
    time.sleep(10)
    produce_post(eventbus)