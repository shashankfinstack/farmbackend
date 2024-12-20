from models.farmer import Farmer
from extensions import db
from mappers.farmer import FarmerMapper

class FarmerRepository:
    # GET 
    # @staticmethod
    # def get_all_farmers(page: int, page_size: int):
    #     try:
    #         farmers = Farmer.query.paginate(page=page, per_page=page_size, error_out=False).items
    #         total_count = Farmer.query.count()
    #         return [FarmerMapper.to_dto(f) for f in farmers], total_count
    #     except Exception as e:
    #         raise e

    @staticmethod
    def get_all_farmers(page: int, page_size: int):
        try:
            query = Farmer.query
            total_count = query.count()
            farmers = query.paginate(page=page, per_page=page_size, error_out=False).items
            return [FarmerMapper.to_dto(f) for f in farmers], total_count
        except Exception as e:
            raise e
        

    @staticmethod
    def get_farmer_by_id(id):
        try:
            farmer = Farmer.query.get(id)
            if farmer:
                return FarmerMapper.to_dto(farmer)          # Returning FarmerDTO
            return None
        except Exception as e:
            raise e
        
    
    @staticmethod
    def get_farmers_by_crop(crop_grown):
        try:
            farmers = Farmer.query.join(Farmer.farms).filter_by(crop_grown=crop_grown).all()
            return [FarmerMapper.to_dto(f) for f in farmers]  # Returning list of FarmerDTO
        except Exception as e:
            raise e
    
    # CREATE 
    @staticmethod
    def create_farmer(phone_number, name, language, country_id):
        if Farmer.query.filter_by(phone_number=phone_number, country_id=country_id).first():
            return None, "Farmer already exists with this phone number and country"

        farmer = Farmer(phone_number=phone_number, name=name, language=language, country_id=country_id)
        db.session.add(farmer)
        db.session.commit()
        return FarmerMapper.to_dto(farmer), None
    
    # UPDATE 
    @staticmethod
    def update_farmer_by_id(id, phone_number, name, language, country_id):
        try:
            farmer = Farmer.query.get(id)
            if not farmer:
                return None, "Farmer not found"

            farmer.phone_number = phone_number
            farmer.name = name
            farmer.language = language
            farmer.country_id = country_id

            db.session.commit()
            return FarmerMapper.to_dto(farmer), None  # Return the updated FarmerDTO
        except Exception as e:
            db.session.rollback()
            raise e
    
    # DELETE 
    @staticmethod
    def delete_farmer_by_id(id):
        try:
            farmer = Farmer.query.get(id)
            if not farmer:
                return {"message": "Farmer not found"}, 404

            db.session.delete(farmer)
            db.session.commit()
            return {"message": "Farmer deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            raise e