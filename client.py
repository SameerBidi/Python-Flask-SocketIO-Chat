import socketio

sio = socketio.Client()

def startMessageLoop():
  while(True):
    try:
      print("\n1: Send public message\n2: Send private message to a user\n")
      opt = int(input("Enter your choice: "))
      if(opt == 1):
        msg = input("Enter your message: ")
        sio.emit("sendPublic", {"fromUser": name, "message": msg})
      elif(opt == 2):
        msg = input("Enter your message: ")
        user = input("Who do you want to send message?: ")
        sio.emit("sendPrivate", {"fromUser": name, "message": msg, "toUser": user})
      opt = input("Do you wan to continue? Y/N: ")
      if(opt == "N" or opt == "n"): 
        sio.disconnect()
        break
    except: continue

@sio.event
def connect():
  print("\nConnected to server")
  startMessageLoop()

@sio.event
def disconnect():
  print("\nDisconnected from server")

name = input("Enter your name: ")
if name:
  sio.connect("http://localhost:5000")

@sio.on("public")
def onPublic(data):
  print(f"\n\nGot Public Message\nFrom: {data['fromUser']}\nMessage: {data['message']}")

@sio.on(f"private:{name}")
def onPrivate(data):
  print(f"\n\nGot Private Message\nFrom: {data['fromUser']}\nMessage: {data['message']}")

sio.wait()