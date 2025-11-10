from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
import jwt
import datetime

auth_bp = Blueprint('auth', __name__)

# Dummy user store
users = {}

SECRET_KEY = 'supersecretkey'

@auth_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    if username in users:
        return jsonify({'message': 'User already exists'}), 400
    hashed_password = generate_password_hash(password, method='sha256')
    users[username] = {'password': hashed_password, 'profile': {}}
    return jsonify({'message': 'User created successfully'})

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')
    user = users.get(username)
    if not user or not check_password_hash(user['password'], password):
        return jsonify({'message': 'Invalid credentials'}), 401
    token = jwt.encode({'user': username, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}, SECRET_KEY, algorithm='HS256')
    return jsonify({'token': token})

@auth_bp.route('/profile', methods=['GET', 'PUT'])
def profile():
    token = None
    if 'Authorization' in request.headers:
        token = request.headers['Authorization'].split(' ')[1]
    if not token:
        return jsonify({'message': 'Token is missing!'}), 401
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        username = data['user']
    except:
        return jsonify({'message': 'Token is invalid!'}), 401
    if request.method == 'GET':
        return jsonify(users[username]['profile'])
    elif request.method == 'PUT':
        profile_data = request.json
        users[username]['profile'] = profile_data
        return jsonify({'message': 'Profile updated'})
