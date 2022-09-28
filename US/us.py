import json
import requests
from socket import *
from flask import Flask,request,Response

app = Flask(__name__)

@app.route('/fibonacci',methods = ['GET'])
def us():
    hostname = request.args["hostname"]
    fs_port = request.args["fs_port"]
    x = request.args["number"]
    as_ip = request.args["as_ip"]
    as_port = request.args["as_port"]
    if hostname == "" or fs_port == "" or x == "" or as_ip == "" or as_port == "":
        Response("Bad format", status=400)
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    data = {
        "NAME": hostname,
        "TYPE": "A"
    }
    clientSocket.sendto(json.dumps(data).encode(),(as_ip, as_port))
    modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
    message = modifiedMessage.decode()
    response = json.loads(message)
    output_result = requests.get("http://"+response["VALUE"]+":"+fs_port+"/fibonacci?"+"number="+x)
    return output_result,Response(status=200)

app.run(host='0.0.0.0',port=8080,debug=True)