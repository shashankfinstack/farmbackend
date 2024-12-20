from models.user import User
from dtos.user_dto import UserDTO

class UserMapper:
    @staticmethod
    def to_dto(user: User) -> UserDTO:
        # Converts a User domain model into a UserDTO.
        return UserDTO(
            id = user.id,
            username = user.username,
            roles = user.roles,
            password_hash = user.password_hash
        )

    @staticmethod
    def to_model(user_dto: UserDTO) -> User:
        # Converts a UserDTO back into a User domain model.
        user = User(
            id = user_dto.id,
            username = user_dto.username,
            roles = user_dto.roles,
            password_hash = user_dto.password_hash
        )
        return user
    


# The UserMapper class is used to convert between the User model (which represents the user in the database) and 
# the UserDTO (which is a simplified object used to interact with the outside world, like in API responses or requests).