from extensions import db

class Farmer(db.Model):
    __tablename__ = 'farmers'

    id = db.Column(db.Integer, primary_key = True,autoincrement=True)
    phone_number = db.Column(db.String, unique = True, nullable = False)
    name = db.Column(db.String, nullable = False)
    language = db.Column(db.String)
    country_id = db.Column(db.Integer, db.ForeignKey('countries.id'))

    country = db.relationship("Country", back_populates = "farmers")
    farms = db.relationship("Farm", back_populates = "farmer", cascade = "all, delete-orphan")      # Deletes child objects that are no longer associated with a parent.

    def __repr__(self):
        return f"<Farmer(id={self.id}, name={self.name}, phone_number={self.phone_number})>"

# this model represents a farmer in the database. Each farmer is associated with a country and can own multiple farms
# country_id (Integer, ForeignKey)
# Foreign key linking the farmer to a specific country (countries.id)
# establishes a relationship between the Farmer and Country models

# __repr__  -> rovides a readable string representation of the Farmer object
# farmer = Farmer(id=1, name="John Doe", phone_number="+919876543210")
# print(farmer)
# Output: <Farmer(id=1, name=John Doe, phone_number=+919876543210)>
