from socket import *
import json
from flask import Response

serverPort = 53533
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print("The server is ready to receive")

while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    message = json.loads(modifiedMessage)
    if not message["VALUE"]:
        with open("run.json","r") as runfile:
            data = json.load(runfile)
        DNS_response = data[message["NAME"]]
        dns_message = json.dumps(DNS_response)
        serverSocket.sendto(dns_message.encode(),clientAddress)
        Response(status=200)
    else:
        data = {message["NAME"]:message}
        reg = json.dumps(data)
        with open("run.json","w") as runfile:
            runfile.write(reg)
        serverSocket.sendto(str(201).encode(), clientAddress)
        Response("Registration is successful", status=201)
