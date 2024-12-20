from models.user import User
from sqlalchemy.orm.attributes import flag_modified
from mappers.user import UserMapper
from extensions import db
from sqlalchemy.exc import SQLAlchemyError

class UserRepository:

    @staticmethod
    def find_by_username(username):
        try:
            user = User.query.filter_by(username=username).first()
            return UserMapper.to_dto(user) if user else None
        except SQLAlchemyError as e:
            print(f"Error finding user by username: {e}")
            return None

    @staticmethod
    def find_by_id(user_id):
        try:
            user = User.query.get(user_id)
            return UserMapper.to_dto(user) if user else None
        except SQLAlchemyError as e:
            print(f"Error finding user by ID: {e}")
            return None

    @staticmethod
    def save(user):
        try:
            db.session.add(user)
            db.session.commit()
            return UserMapper.to_dto(user)
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error saving user: {e}")
            raise

    @staticmethod
    def update(user):
        try:
            flag_modified(user, 'roles')
            db.session.merge(user)
            db.session.commit()
            return UserMapper.to_dto(user)
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error updating user: {e}")
            raise

    @staticmethod
    def delete(user):
        try:
            db.session.delete(user)
            db.session.commit()
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error deleting user: {e}")
            raise

    @staticmethod
    def count():
        try:
            return User.query.count()
        except SQLAlchemyError as e:
            print(f"Error counting users: {e}")
            return 0
        
    @staticmethod
    def delete_by_id(user_id):
        try:
            user = User.query.get(user_id)
            if user:
                db.session.delete(user)
                db.session.commit()
            else:
                print(f"User with ID {user_id} not found")
        except SQLAlchemyError as e:
            db.session.rollback()
            print(f"Error deleting user by ID: {e}")
            raise
    
    @staticmethod
    def getAllUsers():
        try:
            users = User.query.all()
            return [UserMapper.to_dto(user) for user in users] if users else None
        except Exception as e:
            raise