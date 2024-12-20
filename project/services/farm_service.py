from repositories.farm_repo import FarmRepository
from mappers.farm import FarmMapper

class FarmService:

    @staticmethod
    def get_all_farms():
        try:
            farms = FarmRepository.get_all_farms()
            return [f.as_dict() for f in farms]                # Returning list of FarmDTO as dictionaries
        except Exception as e:
            raise e

    @staticmethod
    def get_farm_by_id(farm_id):
        try:
            farm = FarmRepository.get_farm_by_id(farm_id)
            if farm:
                return farm.as_dict()               # Returning FarmDTO as dictionary
            return None
        except Exception as e:
            raise e

    @staticmethod
    def create_farm(area, village, crop_grown, sowing_date, farmer_id, country_id):
        try:
            farm, error = FarmRepository.create_farm(area, village, crop_grown, sowing_date, farmer_id, country_id)
            if error:
                return {"error": error}, 400

            return farm.as_dict(), 201              # Returning FarmDTO as dictionary
        except Exception as e:
            return {"error": str(e)}, 500
    
    @staticmethod
    def get_farms_by_farmer_id(farmer_id):
        try:
            farms = FarmRepository.get_farms_by_farmer_id(farmer_id)
            return [f.as_dict() for f in farms]       # Returning list of FarmDTO as dictionaries
        except Exception as e:
            raise e
        
    @staticmethod
    def update_farm_by_id(farm_id, area, village, crop_grown, sowing_date, farmer_id, country_id):
        try:
            farm, error = FarmRepository.update_farm_by_id(farm_id, area, village, crop_grown, sowing_date, farmer_id, country_id)
            if error:
                return {"error": error}, 400

            return farm.as_dict(), 200             # Return the updated FarmDTO as a dictionary
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def delete_farm_by_id(farm_id):
        try:
            response, status = FarmRepository.delete_farm_by_id(farm_id)
            return response, status
        except Exception as e:
            return {"error": str(e)}, 500
        



    # @staticmethod
    # def get_all_farms():
    #     try:
    #         farms = FarmRepository.get_all_farms()
    #         return [FarmMapper.to_dto(farm).as_dict() for farm in farms]  # Use FarmMapper to convert to FarmDTO
    #     except Exception as e:
    #         raise e

    # @staticmethod
    # def get_farm_by_id(farm_id):
    #     try:
    #         farm = FarmRepository.get_farm_by_id(farm_id)
    #         if farm:
    #             return FarmMapper.to_dto(farm).as_dict()  # Convert Farm to FarmDTO
    #         return None
    #     except Exception as e:
    #         raise e

    # @staticmethod
    # def create_farm(area, village, crop_grown, sowing_date, farmer_id, country_id):
    #     try:
    #         farm, error = FarmRepository.create_farm(area, village, crop_grown, sowing_date, farmer_id, country_id)
    #         if error:
    #             return {"error": error}, 400

    #         return FarmMapper.to_dto(farm).as_dict(), 201  # Convert the created Farm to FarmDTO
    #     except Exception as e:
    #         return {"error": str(e)}, 500

    # @staticmethod
    # def get_farms_by_farmer_id(farmer_id):
    #     try:
    #         farms = FarmRepository.get_farms_by_farmer_id(farmer_id)
    #         return [FarmMapper.to_dto(farm).as_dict() for farm in farms]  # Convert each Farm to FarmDTO
    #     except Exception as e:
    #         raise e

    # @staticmethod
    # def update_farm_by_id(farm_id, area, village, crop_grown, sowing_date, farmer_id, country_id):
    #     try:
    #         farm, error = FarmRepository.update_farm_by_id(farm_id, area, village, crop_grown, sowing_date, farmer_id, country_id)
    #         if error:
    #             return {"error": error}, 400

    #         return FarmMapper.to_dto(farm).as_dict(), 200  # Convert the updated Farm to FarmDTO
    #     except Exception as e:
    #         return {"error": str(e)}, 500

    # @staticmethod
    # def delete_farm_by_id(farm_id):
    #     try:
    #         response, status = FarmRepository.delete_farm_by_id(farm_id)
    #         return response, status
    #     except Exception as e:
    #         return {"error": str(e)}, 500