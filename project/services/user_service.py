from models.user import User
from repositories.user_repo import UserRepository
from mappers.user import UserMapper
from flask_jwt_extended import create_access_token  
import datetime, bcrypt

class UserService:

            
    @staticmethod
    def getAllUsers():
        try:
            users = UserRepository.getAllUsers()
            if not users:
                return {"error":"No Users found"}, 404
            return [user.as_dict() for user in users], 200
        except Exception as e:
            return {"error": f"Internal server error, {str(e)}"}, 500

    @staticmethod
    def create_user(username, password):
        try:
            if UserRepository.find_by_username(username):
                return {"error": "User already exists"}, 400

            password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            user = User(username=username, password_hash=password_hash)
            UserRepository.save(user)

            return {"message": "User created successfully"}, 201
        except Exception as e:
            print(f"Error creating user: {e}", flush=True)
            return {"error": "Internal server error"}, 500


    @staticmethod
    def authenticate_user(username, password):
        try:
            user_dto = UserRepository.find_by_username(username)
            if not user_dto:
                return {"error": "Invalid credentials"}, 401

            user_model = UserMapper.to_model(user_dto)
            if bcrypt.checkpw(password.encode('utf-8'), user_model.password_hash.encode('utf-8')):
                expires = datetime.timedelta(hours=1)
                access_token = create_access_token(identity={"username": user_dto.username, "roles": user_dto.roles}, expires_delta=expires)
                return {"message": "Login successful", "access_token": access_token, "roles": user_dto.roles}, 200
            else:
                return {"error": "Invalid credentials"}, 401
        except Exception as e:
            print(f"Error authenticating user: {e}", flush=True)
            return {"error": "Internal server error"}, 500

    @staticmethod
    def make_admin(user_id):
        try:
            user_dto = UserRepository.find_by_id(user_id)
            if not user_dto:
                return {"error": "User not found"}, 404

            user_model = UserMapper.to_model(user_dto)
            if user_model.has_role('admin'):
                return {"message": "User is already an admin"}, 400

            user_model.add_role('admin')
            UserRepository.update(user_model)
            return {"message": "User is now an admin"}, 200
        except Exception as e:
            print(f"Error making user admin: {e}", flush=True)
            return {"error": "Internal server error"}, 500

    @staticmethod
    def remove_admin(user_id):
        try:
            user_dto = UserRepository.find_by_id(user_id)
            if not user_dto:
                return {"error": "User not found"}, 404

            user_model = UserMapper.to_model(user_dto)
            if not user_model.has_role('admin'):
                return {"error": "User is not an admin"}, 400

            user_model.remove_role('admin')
            UserRepository.update(user_model)
            return {"message": "Admin role removed from user"}, 200
        except Exception as e:
            print(f"Error removing admin role: {e}")
            return {"error": "Internal server error"}, 500

    @staticmethod    
    def delete_user_by_id(user_id):
        try:
            user_dto = UserRepository.find_by_id(user_id)
            if not user_dto:
                return {"error": "User not found"}, 404

            UserRepository.delete_by_id(user_id)
            return {"message": "User deleted successfully"}, 200
        except Exception as e:
            print(f"Error deleting user by ID: {e}", flush=True)
            return {"error": "Internal server error"}, 500
