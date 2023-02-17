from flask import Flask, request, session

consumers = Flask(__name__)

@consumers.route('/notification', methods=["POST"])
def notification_consumer():
    return "Success"

@consumers.route('/post', methods=["POST"])
def post_consumer():
    form = request.get_json()
    event = events[form.pop("Type")]
    event = event(**form)
    return "Success"

if __name__ == "__main__":
    consumers.run(port=5000)