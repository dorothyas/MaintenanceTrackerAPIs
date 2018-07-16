from flask import Flask, jsonify, request #import flask library relevant items from flask model
app = Flask(__name__)

requests =[]
requestId = 0


@app.route('/users/requests',methods=['POST'])
def addRequest():
    userRequest = {'Equipment Name': request.json['Equipment Name'], 
                    'serial number': request.json['serial number'], 
                    'floor number':request.json['floor number'], 
                    'brief description':request.json['brief description']
                    'requestId': request.json['requestId']}
    requests.append(userRequest)
    return jsonify({'requests': requests})

@app.route('/users/requests',methods=['GET'])
def allRequests():
    return jsonify({'requests' : requests})

@app.route('/users/requests/<requestId>',methods=['GET'])
def oneRequest():
    request = [request for request in requests if request ['requestid'] == requestid]
    return jsonify({'request' : requestId [0]})


@app.route('/users/requests/<requestId>',methods=['PUT'])
def editRequest():
    requestId = [request for request in requests if request ['id'] == id]
    requestId[0]['id']=request.json['id']
    return jsonify({'request': requestId [0]})

if __name__=='__main__':
     app.run(debug=True)
