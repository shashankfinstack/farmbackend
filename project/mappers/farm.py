from models.farms import Farm
from dtos.farm_dto import FarmDTO

class FarmMapper:
    @staticmethod
    def to_dto(farm: Farm) -> FarmDTO:
        # Converts a Farm domain model into a FarmDTO for use in external layers 
        # (e.g., API responses, service-to-service communication).
        return FarmDTO(
            id = farm.id,
            area = farm.area,
            village = farm.village,
            crop_grown = farm.crop_grown,
            sowing_date = farm.sowing_date,
            farmer_id = farm.farmer_id,
            country_id = farm.country_id
        )
    
    @staticmethod
    def to_model(farm_dto: FarmDTO) -> Farm:
        # Converts a FarmDTO into a Farm domain model for internal use, such as persisting data into 
        # the database or performing business logic operations.
        return Farm(
            id = farm_dto.id,
            area = farm_dto.area,
            village = farm_dto.village,
            crop_grown = farm_dto.crop_grown,
            sowing_date = farm_dto.sowing_date,
            farmer_id = farm_dto.farmer_id,
            country_id = farm_dto.country_id
        )
    

# It is responsible for converting between the internal model (Farm) and the Data Transfer Object (DTO, FarmDTO).
# The FarmMapper class helps transform the internal Farm model to the FarmDTO that is used to transfer data externally, 
# typically in API responses.