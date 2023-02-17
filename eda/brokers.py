import requests

class EventBus:
    def __init__(self):
        self.subscribers = {}
        self.queue = []

    def subscribe(self, event_type, subscriber) -> None:
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(subscriber)
        print(subscriber)

    def unsubscribe(self, event_type, subscriber) -> None:
        if event_type not in self.subscribers:
            return
        self.subscribers[event_type].remove(subscriber)

    def notify(self, event):
        if str(event.__class__.__name__) not in self.subscribers:
            return
        for subscriber in self.subscribers[str(event.__class__.__name__)]:
            res = requests.post('http://127.0.0.1:5000' + subscriber, json=event.to_repr)
            print(res)
            yield res

    def give_event(self, event) -> None:
        self.queue.append(event)

    def listen(self) -> bool:
        while self.queue != []:
            print(self.queue)
            self.notify(self.queue.pop(0))
            # self.elastic_growth()
        return True
    
    # def elastic_growth(self):
    #     totals = {}
    #     for event in self.queue:
    #         if event not in totals:
    #             totals[event] = 1
    #         else:
    #             totals[event] += 1
        

