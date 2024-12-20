from repositories.country_repo import CountryRepository
from dtos.country_dto import CountryDTO

class CountryService:
    
    @staticmethod
    def get_all_countries():
        try:
            countries = CountryRepository.get_all_countries()
            return [c.as_dict() for c in countries]          # Returning list of CountryDTO as dictionaries
        except Exception as e:
            raise e
        
    
    @staticmethod
    def get_country_by_id(id):
        try:
            country = CountryRepository.get_country_by_id(id)
            if country:
                return country.as_dict()                    # Returning CountryDTO as dictionary
            return None
        except Exception as e:
            raise e
    
    @staticmethod
    def add_country(name):
        try:
            country, error = CountryRepository.add_country(name)
            if error:
                return {"error": error}, 400
            
            return country.as_dict(), 201                  # Returning CountryDTO as dictionary
        except Exception as e:
            return {"error": str(e)}, 500
        
    
    @staticmethod
    def update_country_by_id(id, name):
        try:
            country, error = CountryRepository.update_country_by_id(id, name)
            if error:
                return {"error": error}, 400

            return country.as_dict(), 200                   # Returning CountryDTO as dictionary
        except Exception as e:
            return {"error": str(e)}, 500

    @staticmethod
    def delete_country_by_id(id):
        try:
            response, status = CountryRepository.delete_country_by_id(id)
            return response, status
        except Exception as e:
            return {"error": str(e)}, 500