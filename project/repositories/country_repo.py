from sqlalchemy import func
from models.countries import Country
from extensions import db
from mappers.country import CountryMapper 

class CountryRepository:
    # GET 
    # Process: Executes Country.query.all() to retrieve all country records from the database.
    # Converts the result (a list of Country model instances) into a list of CountryDTO objects using the CountryMapper.
    @staticmethod
    def get_all_countries():
        try:
            countries = Country.query.all()
            return [CountryMapper.to_dto(c) for c in countries]        # Returning list of CountryDTO
        except Exception as e:
            raise e
    
    # Uses Country.query.get(id) to retrieve a single record by its primary key.
    # If the country exists, converts it to a CountryDTO using CountryMapper, else return None if not found
    @staticmethod
    def get_country_by_id(id):
        try:
            country = Country.query.get(id)
            if country:
                return CountryMapper.to_dto(country)                   # Returning CountryDTO
            return None
        except Exception as e:
            raise e
    
    # ADD 
    @staticmethod
    def add_country(name):
        try:
            existing_country = Country.query.filter(func.lower(Country.name) == func.lower(name)).first()
            if existing_country:
                return None, "Country already exists"
            
            country = Country(name=name)
            db.session.add(country)
            db.session.commit()
            return CountryMapper.to_dto(country), None  
        except Exception as e:
            raise e
    
    # UPDATE 
    @staticmethod
    def update_country_by_id(id, name):
        try:
            country = Country.query.get(id)
            if not country:
                return None, "Country not found"

            existing_country = Country.query.filter(func.lower(Country.name) == func.lower(name)).first()
            if existing_country and existing_country.id != id:
                return None, "Country name already exists"

            country.name = name
            db.session.commit()
            return CountryMapper.to_dto(country), None  # Returning CountryDTO
        except Exception as e:
            db.session.rollback()
            raise e
    
    # DELETE 
    @staticmethod
    def delete_country_by_id(id):
        try:
            country = Country.query.get(id)
            if not country:
                return {"message": "Country not found"}, 404

            db.session.delete(country)
            db.session.commit()
            return {"message": "Country deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            raise e


    