from flask import Flask, jsonify, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

#HACK1
@app.route('/users', methods=['GET']) 
def get_users(): 
    response = {'payload': 'success'} 
    return jsonify(response)

#HACK2
@app.route('/user', methods=['POST']) 
def create_user(): 
    response = {'payload': 'success'} 
    return jsonify(response)

#HACK3
@app.route('/user', methods=['DELETE']) 
def delete_user(): 
    response = {'payload': 'success'} 
    return jsonify(response)

#HACK4
@app.route('/user', methods=['PUT'])
def update_user(): 
    response = {'payload': 'success'} 
    return jsonify(response)

#HACK5
@app.route('/api/v1/users', methods=['GET'])
def get_user():
    response = {'payload': []}
    return jsonify(response)

#HACK6
@app.route('/api/v1/user', methods=['POST'])
def send_user_data():
    email = request.args.get('email')
    name = request.args.get('name')
    
    response = {
        'payload': {
            'email': email,
            'name': name,
        }
    }
    return jsonify(response)

#HACK7
@app.route('/api/v1/user/add', methods=['POST'])
def send_user_form():
    email = request.form.get('email')
    name = request.form.get('name')
    id = request.form.get('id')
    
    response = {
        'payload': {
            'email': email,
            'name': name,
            'id': id,
        }
    }
    return jsonify(response)

#HACK8
@app.route('/api/v1/user/create', methods=['POST'])
def send_user_json():
    # Obtiene los datos JSON enviados en la solicitud
    data = request.get_json()
    email = data['email']
    name = data['name']
    id = data['id']
    
    response = {
        'payload': {
            'email': email,
            'name': name,
            'id': id,
        }
    }
    return jsonify(response)


if __name__ == "__main__":
    app.run(debug=True)