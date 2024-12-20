from flask import Blueprint, request, jsonify, session
from decorators import role_required, Role
from services.user_service import UserService

user_blueprint = Blueprint('user', __name__)
    
@user_blueprint.route('/all', methods=['GET'])
@role_required()
def allUsers():
    try: 
        response, status = UserService.getAllUsers()     
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": f"Internal Server Error: {str(e)}"}), 500


@user_blueprint.route('/create-user', methods=['POST']) 
@role_required([Role.ADMIN])
def create_user():
    try:
        data = request.get_json()
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({"error": "Username and password are required"}), 400

        username = data['username']
        password = data['password']

        response, status = UserService.create_user(username, password)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500

@user_blueprint.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()
        if not data or 'username' not in data or 'password' not in data:
            return jsonify({"error": "Username and password are required"}), 400

        username = data['username']
        password = data['password']

        response, status = UserService.authenticate_user(username, password)
        return jsonify(response), status
    except Exception as e:
        print("Exception caught", e, flush=True)
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500
    
@user_blueprint.route('/logout', methods=['POST'])
def logout():
    try:
        # using Flask sessions
        session.clear()        
        return jsonify({"message": "Logout successful"}), 200
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


@user_blueprint.route('/make-admin/<int:user_id>', methods=['PUT'])
@role_required([Role.ADMIN])
def make_admin(user_id):
    try:
        response, status = UserService.make_admin(user_id)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


@user_blueprint.route('/remove-admin/<int:user_id>', methods=['PUT'])
@role_required([Role.ADMIN])
def remove_admin(user_id):
    try:
        response, status = UserService.remove_admin(user_id)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500


@user_blueprint.route('/delete-user/<int:user_id>', methods=['DELETE'])
@role_required([Role.SUPERADMIN])
def delete_user(user_id):
    try:
        response, status = UserService.delete_user_by_id(user_id)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": f"Internal server error: {str(e)}"}), 500
