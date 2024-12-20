from extensions import db

class Farm(db.Model):
    __tablename__ = 'farms'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    area = db.Column(db.String, nullable=False)
    village = db.Column(db.String, nullable=False)
    crop_grown = db.Column(db.String, nullable=False)
    sowing_date = db.Column(db.Date, nullable=False)
    farmer_id = db.Column(db.Integer, db.ForeignKey('farmers.id'))
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))

    farmer = db.relationship("Farmer", back_populates="farms")
    country = db.relationship("Country", back_populates="farms")
    schedules = db.relationship("Schedule", back_populates="farm", cascade="all, delete-orphan")       
    # When a farm is deleted, all associated schedules are also deleted.

    def __repr__(self):
        return f"<Farm(id={self.id}, crop_grown={self.crop_grown}, sowing_date={self.sowing_date})>"

# This model represents a farm in the database. It stores details about the location, crop, and sowing activities and links to the farmer and country it belongs to
# farmer_id (Integer, ForeignKey)
# Foreign key linking the farm to a specific farmer (farmers.id)
# establishes a relationship between the Farm and Farmer models
# country_id (Integer, ForeignKey)
# Foreign key linking the farm to a specific country (countries.id)
# establishes a relationship between the Farm and Country models

# __repr__ -> Provides a readable string representation of the Farm object
# farm = Farm(id=1, crop_grown="Wheat", sowing_date="2024-12-01")
# print(farm)
# Output: <Farm(id=1, crop_grown=Wheat, sowing_date=2024-12-01)>
