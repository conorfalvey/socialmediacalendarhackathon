from flask import Flask, request, session

app = Flask(__name__)


@app.route('/notification', methods=["POST"])
def notification_consumer():
    return "Success"

@app.route('/post', methods=["POST"])
def post_consumer():
    return "Sucess"