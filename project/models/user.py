from sqlalchemy import Column, String, Integer, ARRAY
from extensions import db
import bcrypt

class User(db.Model):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(80), unique=True, nullable=False)
    password_hash = Column(String, nullable=False)
    roles = Column(ARRAY(String), nullable=False, default=["viewer"])  
    # role = Column(String, nullable=False, default="viewer")
    # Roles: "superadmin", "admin", "viewer"

    def set_password(self, password):
        self.password_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    
    def check_password(self, password):
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())

    def has_role(self, role):
        return role in self.roles
    
    def remove_role(self, role):
        if role in self.roles:
            self.roles.remove(role)

    def add_role(self, role):
        print(f"Got call here with {role}", flush=True)
        if role not in self.roles:
            roles = self.roles
            roles.append(role)
            self.roles =roles
        print("Roles of user after updating are", self.roles, flush=True)


# This model represents a user in the application, it stores the user's authentication credentials and their roles/permissions
# since UTF-8 is the default


