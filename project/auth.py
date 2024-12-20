import datetime
import jwt
import bcrypt
from flask import Blueprint, request, jsonify

# Blueprint for auth routes
auth_bp = Blueprint('auth', __name__)

# Secret key for JWT (use environment variables in production)
SECRET_KEY = "ae4fd98e444bd859f1947549d53531d8f084fd84bd2ee5b95f438572a4bc5c9e"

# Mock user database
users_db = {
    "test_user": bcrypt.hashpw("test_password".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
    "gaurav": bcrypt.hashpw("gaurav".encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
}

# Route to handle user login
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "Username and password required"}), 400

    user_password_hash = users_db.get(username)
    if not user_password_hash or not bcrypt.checkpw(password.encode('utf-8'), user_password_hash.encode('utf-8')):
        return jsonify({"error": "Invalid credentials"}), 401

    # Generate JWT token
    token = jwt.encode(
        {
            "username": username,
            "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
        },
        SECRET_KEY,
        algorithm="HS256",
    )
    return jsonify({"token": token}), 200

# Route to handle protected resource access
@auth_bp.route('/protected', methods=['GET'])
def protected():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token missing"}), 401

    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return jsonify({"message": f"Welcome {decoded_token['username']}!"}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token has expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 401








# import datetime
# import jwt
# from flask import Blueprint, request, jsonify
# from werkzeug.security import check_password_hash, generate_password_hash

# # Blueprint for auth routes
# auth_bp = Blueprint('auth', __name__)

# # Secret key for JWT (use environment variables in production)
# SECRET_KEY = "ae4fd98e444bd859f1947549d53531d8f084fd84bd2ee5b95f438572a4bc5c9e"

# # Mock user database
# users_db = {
#     "test_user": generate_password_hash("test_password"),
# }

# # Route to handle user login
# @auth_bp.route('/login', methods=['POST'])
# def login():
#     data = request.get_json()
#     username = data.get("username")
#     password = data.get("password")

#     if not username or not password:
#         return jsonify({"error": "Username and password required"}), 400

#     user_password_hash = users_db.get(username)
#     # if not user_password_hash or not check_password_hash(user_password_hash, password):
#     #     return jsonify({"error": "Invalid credentials"}), 401

#     if not check_password_hash(user_password_hash, password):
#         return jsonify({"error": "Invalid credentials"}), 401

#     # Generate JWT token
#     token = jwt.encode(
#         {
#             "username": username,
#             "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=1),
#         },
#         SECRET_KEY,
#         algorithm="HS256",
#     )
#     return jsonify({"token": token}), 200

# # Route to handle protected resource access
# @auth_bp.route('/protected', methods=['GET'])
# def protected():
#     token = request.headers.get("Authorization")
#     if not token:
#         return jsonify({"error": "Token missing"}), 401

#     try:
#         decoded_token = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
#         return jsonify({"message": f"Welcome {decoded_token['username']}!"}), 200
#     except jwt.ExpiredSignatureError:
#         return jsonify({"error": "Token has expired"}), 401
#     except jwt.InvalidTokenError:
#         return jsonify({"error": "Invalid token"}), 401



