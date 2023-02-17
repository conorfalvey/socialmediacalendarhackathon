import time
from brokers import EventBus 
from producers import produce, produce_post
from consumers import Consumer
from events import PostEvent

# while True:
eventbus = EventBus()
eventbus.subscribe(PostEvent(), Consumer())
print("Eventbus set up")

produce_post(eventbus)
while eventbus.listen():
    print("Time sleep")
    time.sleep(10)
    print("Time awake")
    produce_post(eventbus)
