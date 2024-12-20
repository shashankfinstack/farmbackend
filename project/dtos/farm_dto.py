class FarmDTO:
    def __init__(self, id: int, area: str, village: str, crop_grown: str, sowing_date: str, farmer_id: int, country_id: int):
        self.id = id 
        self.area = area
        self.village = village
        self.crop_grown = crop_grown
        self.sowing_date = sowing_date
        self.farmer_id = farmer_id
        self.country_id = country_id

    def as_dict(self):
        return {
            "id": self.id,
            "area": self.area,
            "village": self.village,
            "crop_grown": self.crop_grown,
            "sowing_date": self.sowing_date,
            "farmer_id": self.farmer_id,
            "country_id": self.country_id
        }
    

# Represents a farm owned by a farmer in a specific country.