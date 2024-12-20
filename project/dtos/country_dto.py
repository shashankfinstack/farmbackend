class CountryDTO:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

    def as_dict(self):
        return {
            "id": self.id,
            "name": self.name
        }

# id (int): Unique identifier for the country
# name (str): Name of the country

# Represents a country in the system, used for grouping farmers and farms by country.