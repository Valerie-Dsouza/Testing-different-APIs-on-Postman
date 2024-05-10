

import logging
import sys
sys.path.append("./")
from signalrcore.hub_connection_builder import HubConnectionBuilder

server_url = "wss://localhost:6001/chathub"
username = input("enter username")

hub_connection = HubConnectionBuilder()\
    .with_url(server_url, options={"verify_ssl": False}).build()
hub_connection.on_open(lambda: print("connection opened and handshake received ready to send messages"))
hub_connection.on_close(lambda: print("connection closed"))

hub_connection.on("ReceiveMessage", print)
hub_connection.start()


while True:
    message = input(" ")
    if message == "exit":
        break
    if message is not None and message != "":
        hub_connection.send("SendMessage", [username, message])

# hub_connection.stop()