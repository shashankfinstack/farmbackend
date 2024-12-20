class ScheduleDTO:
    def __init__(self, id: int, days_after_sowing: int, fertiliser: str, quantity: int, quantity_unit: str, farm_id: int, price_per_unit: int):
        self.id = id
        self.days_after_sowing = days_after_sowing
        self.fertiliser = fertiliser
        self.quantity = quantity
        self.quantity_unit = quantity_unit
        self.farm_id = farm_id
        self.price_per_unit = price_per_unit

    def as_dict(self):
        return {
            "id": self.id,
            "days_after_sowing": self.days_after_sowing,
            "fertiliser": self.fertiliser,
            "quantity": self.quantity,
            "quantity_unit": self.quantity_unit,
            "farm_id": self.farm_id,
            "price_per_unit": self.price_per_unit
        }
    

# Represents a fertilisation schedule for a farm.