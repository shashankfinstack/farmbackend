class UserDTO:
    def __init__(self, username: str, id: int, roles: list, password_hash: str = None):
        self.id = id
        self.username = username
        self.roles = roles
        self.password_hash = password_hash                # Optional, used internally if needed

    def as_dict(self, include_sensitive: bool = False):
        # Exclude sensitive data by default
        user_dict = {
            "id": self.id,
            "username": self.username,
            "roles": self.roles,
        }
        if include_sensitive:
            user_dict["password_hash"] = self.password_hash
        return user_dict



# class UserDTO:
#     def __init__(self, username: str, id: int, password_hash: str, roles: list):
#         self.id = id
#         self.username = username
#         self.password_hash = password_hash
#         self.roles = roles

#     def as_dict(self):
#         return {
#             "id": self.id,
#             "username": self.username,
#             "password_hash":self.password_hash,
#             "roles": self.roles,
#         }


# represents a user of the system (eg admin, farmer, or other roles)
# Eg -> user = UserDTO(username="admin", id=1, password_hash="hashed_pw", roles=["admin", "manager"])
# print(user.as_dict())
# Output: {'id': 1, 'username': 'admin', 'password_hash': 'hashed_pw', 'roles': ['admin', 'manager']}

# Relationships:
# CountryDTO is at the top level and is associated with multiple farmers and farms.
# FarmerDTO is linked to FarmDTO (one-to-many).
# FarmDTO is linked to ScheduleDTO (one-to-many).
# UserDTO is for managing application users and does not directly interact with the rest of the entities.