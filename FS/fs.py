import json
from socket import *
from flask import Flask,request,Response

app = Flask(__name__)

@app.route('/fibonacci',methods = ['GET'])
def fibonacci():
    x = request.args.get("number")
    if x.isdigit():
        x = int(x)
        result = calculate_fibonacci(x)
        return Response("the fibonacci number for "+str(x)+" is "+ str(result), status=200)
    else:
        return Response("Bad format", status=400)

@app.route('/register', methods = ["PUT"])
def register():
    hostname = request.args.get("hostname")
    ip = request.args.get("ip")
    as_ip = request.args.get("as_ip")
    as_port = request.args.get("as_port")
    data = {
        "TYPE": "A",
        "NAME": hostname,
        "VALUE": ip,
        "TTL": 10
    }
    clientSocket = socket(AF_INET, SOCK_DGRAM)
    clientSocket.sendto(json.dumps(data).encode(),(as_ip, as_port))
    return Response("Registration is successful",status=201)

def calculate_fibonacci(x):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    else:
        return calculate_fibonacci(x - 1) + calculate_fibonacci(x - 2)


app.run(host='0.0.0.0',port=9090,debug=True)