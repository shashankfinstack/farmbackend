from repositories.farmer_repo import FarmerRepository
from repositories.schedule_repo import ScheduleRepository

class FarmerService:

    @staticmethod
    def get_all_farmers(page: int, page_size: int):
        try:
            farmers, total_count = FarmerRepository.get_all_farmers(page, page_size)
            return farmers, total_count
        except Exception as e:
            raise e

    @staticmethod
    def get_farmer_by_id(farmer_id):
        try:
            farmer = FarmerRepository.get_farmer_by_id(farmer_id)
            if farmer:
                return farmer.as_dict()  # Returning FarmerDTO as dictionary
            return None
        except Exception as e:
            raise e
        
    @staticmethod
    def get_farmers_by_crop(crop_grown):
        try:
            farmers = FarmerRepository.get_farmers_by_crop(crop_grown)
            return [f.as_dict() for f in farmers]                # Returning list of FarmerDTO as dictionaries
        except Exception as e:
            raise e


    @staticmethod
    def create_farmer(phone_number, name, language, country_id):
        try:
            farmer, error = FarmerRepository.create_farmer(phone_number, name, language, country_id)
            if error:
                return {"error": error}, 400

            return farmer.as_dict(), 201  # Returning FarmerDTO as dictionary
        except Exception as e:
            return {"error": str(e)}, 500
    

    @staticmethod
    def calculate_bill(fertilizer_name, quantity):
        try:
            quantity = float(quantity)
            schedule = ScheduleRepository.get_schedule_by_fertiliser(fertilizer_name)
            
            if not schedule:
                raise ValueError("Fertilizer not found")

            total_cost = schedule.price_per_unit * quantity
            return total_cost
        except ValueError as ve:
            raise ve
        except Exception as e:
            raise e
        
    @staticmethod
    def calculate_bill_of_materials(farmer_id):
        farmer = FarmerRepository.get_farmer_by_id(farmer_id)
        if not farmer:
            raise ValueError("Farmer not found")

        total_cost = 0
        for farm in farmer.farms:
            for schedule in farm.schedules:
                total_cost += schedule.quantity * schedule.price_per_unit

        return total_cost
    
    @staticmethod
    def update_farmer_by_id(id, phone_number, name, language, country_id):
        try:
            farmer, error = FarmerRepository.update_farmer_by_id(id, phone_number, name, language, country_id)
            if error:
                return {"error": error}, 400

            return farmer.as_dict(), 200  # Return the updated FarmerDTO as a dictionary
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def delete_farmer_by_id(id):
        try:
            response, status = FarmerRepository.delete_farmer_by_id(id)
            return response, status
        except Exception as e:
            return {"error": str(e)}, 500