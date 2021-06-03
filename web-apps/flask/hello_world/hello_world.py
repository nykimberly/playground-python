import json
import time

from flask import Flask, request
from typing import Dict, List, Any


app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World!"

chatroom_users = {
    "chat": set()
}
default_chatroom_msg = [
        {
            "author": "chat_help", 
            "msg":"hello, welcome!",
            "timestamp": "0"
        }
    ]
chatroom_msgs: Dict[str, List[Dict[str, Any]]] = {
    "chat": default_chatroom_msg
}

@app.route("/join/<chatroom>/<name>")
def join_chatroom_name(chatroom, name):
    chatroom_users[chatroom].add(name)
    users =  chatroom_users[chatroom]
    return f"welcome to {chatroom}, {len(users)} are here: {users}"

@app.route("/view/<chatroom>")
def view_chatroom(chatroom):
    if not chatroom_msgs.get(chatroom):
        chatroom_msgs[chatroom] = default_chatroom_msg
    return json.dumps(chatroom_msgs.get(chatroom))

@app.route("/post/<chatroom>/<name>", methods = ["POST", "GET"])
def post_chatroom(chatroom, name):
    if chatroom in chatroom_msgs:
        chatroom_msgs[chatroom].append(
            {
                "author": name,
                "msg": request.form.get("msg"),
                "timestamp": time.time()
            }
        )
    return json.dumps(chatroom_msgs.get(chatroom))

if __name__ == "__main__":
    app.run()