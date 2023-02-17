from events import NotificationEvent, PostEvent
import asyncio

def produce(eventbus, event):
    eventbus.give_event(event)

def produce_post(eventbus):
    event = PostEvent(id="Test", platform="Test", delivery_time="Test", text="Test", frequency="Test", user_id="Test")
    eventbus.give_event(event)


def produce_notificaiton(eventbus):
    event = NotificationEvent(email="Test")
    eventbus.give_event(event)