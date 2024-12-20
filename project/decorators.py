from functools import wraps
from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt_identity
from enum import Enum

class Role(Enum):
    ADMIN = 'admin'
    SUPERADMIN = 'superadmin'
    VIEWER = 'viewer'

def role_required(roles=None):
    roles = {role.value for role in (roles or [])}               # Normalize roles as a set of values

    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            try:
                verify_jwt_in_request()
                user_roles = set(get_jwt_identity().get('roles', []))
                # print(user_roles)
                # breakpoint()

                # Allow access for SUPERADMIN or any required role
                if Role.SUPERADMIN.value in user_roles or not roles or roles & user_roles:
                    return f(*args, **kwargs)

                return jsonify({"error": "Access denied"}), 403

            except Exception as e:
                return jsonify({"error": "Login required", "exception": str(e)}), 401

        return decorated_function
    return decorator
