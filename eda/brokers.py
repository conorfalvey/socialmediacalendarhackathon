import requests

class EventBus:
    def __init__(self):
        self.subscribers = {}
        self.queue = []

    def subscribe(self, event_type, subscriber) -> None:
        event_type = str(event_type.__class__.__name__)
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(subscriber)

    def unsubscribe(self, event_type, subscriber) -> None:
        if event_type not in self.subscribers:
            return
        self.subscribers[event_type].remove(subscriber)

    def notify(self, event):
        if str(event.__class__.__name__) not in self.subscribers:
            print("Failed")
            return 
        print(self.subscribers)
        for subscriber in self.subscribers[str(event.__class__.__name__)]:
            print("Notifying...")
            requests.post('http://127.0.0.1:5000' + subscriber, json=event.to_repr())
            print("Finished notify")
            yield res

    def give_event(self, event) -> None:
        self.queue.append(event)

    def listen(self) -> bool:
        while self.queue != []:
            print("QUEUE")
            value = self.queue.pop(0)
            print(value)
            print(str(value.__class__.__name__) in self.subscribers)
            print(value.to_repr())
            self.notify(value)
            print("Notify Done")
            # self.notify(event=None)
        return True
        

