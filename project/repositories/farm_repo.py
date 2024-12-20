from models.farms import Farm
from extensions import db
from mappers.farm import FarmMapper

class FarmRepository:
    # GET 
    @staticmethod
    def get_all_farms():
        try:
            farms = Farm.query.all()
            return [FarmMapper.to_dto(f) for f in farms]         # Returning list of FarmDTO
        except Exception as e:
            raise e
        
    @staticmethod
    def get_farm_by_id(farm_id):
        try:
            farm = Farm.query.get(farm_id)
            if farm:
                return FarmMapper.to_dto(farm)                   # Returning FarmDTO
            return None
        except Exception as e:
            raise e
        
    @staticmethod
    def get_farms_by_farmer_id(farmer_id):
        try:
            farms = Farm.query.filter_by(farmer_id=farmer_id).all()
            return [FarmMapper.to_dto(f) for f in farms]           # Returning list of FarmDTO
        except Exception as e:
            raise e
    

    # ADD
    @staticmethod
    def create_farm(area, village, crop_grown, sowing_date, farmer_id, country_id):
        try:
            existing_farm = Farm.query.filter_by(
                area=area, village=village, crop_grown=crop_grown, 
                sowing_date=sowing_date, farmer_id=farmer_id, country_id=country_id
            ).first()
            if existing_farm:
                return None, "Farm with the same details already exists"
            
            farm = Farm(area=area, village=village, crop_grown=crop_grown, sowing_date=sowing_date, farmer_id=farmer_id, country_id=country_id)
            db.session.add(farm)
            db.session.commit()
            return FarmMapper.to_dto(farm), None  # Returning FarmDTO
        except Exception as e:
            raise e
        

    # UPDATE 
    @staticmethod
    def update_farm_by_id(farm_id, area, village, crop_grown, sowing_date, farmer_id, country_id):
        try:
            farm = Farm.query.get(farm_id)
            if not farm:
                return None, "Farm not found"

            farm.area = area
            farm.village = village
            farm.crop_grown = crop_grown
            farm.sowing_date = sowing_date
            farm.farmer_id = farmer_id
            farm.country_id = country_id

            db.session.commit()
            return FarmMapper.to_dto(farm), None  # Return the updated FarmDTO
        except Exception as e:
            db.session.rollback()
            raise e
    

    # DELETE 
    @staticmethod
    def delete_farm_by_id(farm_id):
        try:
            farm = Farm.query.get(farm_id)
            if not farm:
                return {"message": "Farm not found"}, 404

            db.session.delete(farm)
            db.session.commit()
            return {"message": "Farm deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            raise e