from flask import Flask, request, session
from events import get_event
from app.services.user_service import UserService

consumers = Flask(__name__)


@consumers.route("/notification", methods=["POST"])
def notification_consumer():
    return "Success"


@consumers.route("/post", methods=["POST"])
def post_consumer():
    form = request.get_json()
    event = get_event(form.pop("Type"))
    event = event(**form)
    return "Success"


@consumers.route("/signup", methods=["POST"])
def sign_up_consumer():
    form = request.get_json()
    event = get_event(form.pop("Type"))
    event = event(**form)

    us = UserService()
    us.create_user(
        name=event.name,
        email=event.email,
        password=event.password,
        default_delay=event.default_notification,
    )
    return "Success"


if __name__ == "__main__":
    consumers.run(port=5000)
