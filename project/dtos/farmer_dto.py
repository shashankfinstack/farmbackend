class FarmerDTO:
    def __init__(self, id: int, phone_number: str, name: str, language: str, country_id: int, farms=None):
        self.id = id
        self.phone_number = phone_number
        self.name = name
        self.language = language
        self.country_id = country_id
        self.farms = farms or []

    def as_dict(self):
        return {
            "id": self.id,
            "phone_number": self.phone_number,
            "name": self.name,
            "language": self.language,
            "country_id": self.country_id,
            "farms": [farm.as_dict() for farm in self.farms]
        }
    

# Represents a farmer, including their personal details and farms.