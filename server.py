from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app)

@socketio.on("sendPublic")
def onPublic(data):
  print(f"Public message from {data['fromUser']}")
  emit("public", data, broadcast=True, include_self=False)

@socketio.on("sendPrivate")
def onPublic(data):
  print(f"Private message from: {data['fromUser']} To: {data['toUser']}")
  emit(f"private:{data['toUser']}", data, broadcast=True, include_self=False)

socketio.run(app, host='0.0.0.0')