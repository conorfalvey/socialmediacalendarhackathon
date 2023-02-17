import requests
import json
from flask import Flask, request, session
from events import PostEvent

brokers = Flask(__name__)


subscribers = {}
queue = []

@brokers.route('/short')
def display():
    return str(subscribers) + "\n" + str(queue)

@brokers.route('/short/listen', methods=["POST"])
def listen():
    while queue != []:
        notify(queue.pop(0))
    return "200"

@brokers.route('/short/subscribe', methods=["POST"])
def subscribe() -> None:
    form = request.get_json()
    event_type = form["event_type"]
    subscriber = form["subscriber"]
    if event_type not in subscribers:
        subscribers[event_type] = []
    subscribers[event_type].append(subscriber)
    return "200"

@brokers.route('/short/unsubscribe', methods=["POST"])
def unsubscribe() -> None:
    form = request.get_json()
    event_type = form["event_type"]
    subscriber = form["subscriber"]
    if event_type not in subscribers:
        return
    subscribers[event_type].remove(subscriber)
    return "200"

def notify(event_repr):
    if event_repr["Type"] not in subscribers:
        return
    for subscriber in subscribers[event_repr["Type"]]:
        res = requests.post('http://127.0.0.1:5000' + subscriber, json=event_repr)

events = {
    "PostEvent": PostEvent,
}
@brokers.route('/short/add', methods=["POST"])
def give_event() -> None:
    form = request.get_json()
    queue.append(form)
    return "200"

if __name__ == "__main__":
    brokers.run(port=5001, debug=True)
    # brokers.run(port=5001, debug=False)