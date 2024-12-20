from models.countries import Country
from dtos.country_dto import CountryDTO

class CountryMapper:
    @staticmethod
    def to_dto(country: Country) -> CountryDTO:
        # Converts a domain model into a DTO for data transfer or API responses.
        return CountryDTO(
            id = country.id,
            name = country.name
        )
    
    @staticmethod
    def to_model(country_dto: CountryDTO) -> Country:
        # Converts a DTO into a domain model, often for persisting data back into the database.
        return Country(
            id = country_dto.id,
            name = country_dto.name
        )
    

# The purpose of the CountryMapper class is to convert between the data model (Country) and the Data Transfer Object (DTO) (CountryDTO). 
# This pattern is commonly used to separate the internal data structure of the application from the data exposed to or received from external systems (e.g., REST APIs).