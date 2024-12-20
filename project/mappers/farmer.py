from models.farmer import Farmer
from dtos.farmer_dto import FarmerDTO

class FarmerMapper:
    @staticmethod
    def to_dto(farmer: Farmer) -> FarmerDTO:
        # Converts the internal Farmer model into a FarmerDTO for external use, such as 
        # sending data in API responses or for client consumption.
        return FarmerDTO(
            id = farmer.id,
            phone_number = farmer.phone_number,
            name = farmer.name,
            language = farmer.language,
            country_id = farmer.country_id
        )

    @staticmethod
    def to_model(farmer_dto: FarmerDTO) -> Farmer:
        # Converts the FarmerDTO back into a Farmer domain model for internal operations, 
        # such as database persistence or business logic processing.
        return Farmer(
            id = farmer_dto.id,
            phone_number = farmer_dto.phone_number,
            name = farmer_dto.name,
            language = farmer_dto.language,
            country_id = farmer_dto.country_id
        )
    

# The FarmerMapper class works in the same way as the FarmMapper and 
# CountryMapper classes you've seen earlier, it is responsible for converting between the internal
#  Farmer model (which represents data in the database) and the FarmerDTO (Data Transfer Object) used for sending and receiving data through APIs or other external interfaces.