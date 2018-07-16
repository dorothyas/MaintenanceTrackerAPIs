from flask import Flask, jsonify, request #import flask library relevant items from flask model
app = Flask(__name__)


requests =[]

@app.route('/users/requests',methods=['POST'])
def addRequest():
    userRequest = {'Equipment Name': request.json['Equipment Name'], 
                    'serial number': request.json['serial number'], 
                    'floor number':request.json['floor number'], 
                    'brief description':request.json['brief description'],
                    'requestId' : len(requests) +1}
    requests.append(userRequest)
    return jsonify({'requests': requests})
    


@app.route('/users/requests',methods=['GET'])
def allRequests():
    return jsonify({'requests' : requests})

@app.route('/users/requests/<int:requestId>',methods=['GET'])
def oneRequest(requestId):
    request = [request for request in requests if request ['requestId'] == requestId] 
    return jsonify({'requests' : request})


@app.route('/users/requests/<int:requestId>',methods=['PUT'])
def edit(requestId):
    request1 = [request1 for request1 in requests if request1['requestId'] == requestId]
    request1[0]['floor number'] = request.json['floor number']
    request1[0]['Equipment Name']= request.json['Equipment Name']
    request1[0]['serial number']= request.json['serial number']
    return jsonify({'request': request1})

if __name__=='__main__':
     app.run(debug=True)