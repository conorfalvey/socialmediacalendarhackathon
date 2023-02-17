import asyncio

class EventBus:
    def __init__(self):
        self.subscribers = {}
        self.queue = []

    def subscribe(self, event_type, subscriber):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(subscriber)

    def unsubscribe(self, event_type, subscriber):
        if event_type not in self.subscribers:
            return
        self.subscribers[event_type].remove(subscriber)

    def notify(self, event):
        if str(event.__class__.__name__) not in self.subscribers:
            print("ended")
            return
        for subscriber in self.subscribers[str(event.__class__.__name__)]:
            # yield asyncio.run(subscriber(event))
            yield subscriber(event)

    def give_event(self, event):
        self.queue.append(event)

    def listen(self):
        while self.queue != []:
            print(self.queue)
            self.notify(self.queue.pop(0))
        return True
    

    # def create_consumers(self):
        # 
