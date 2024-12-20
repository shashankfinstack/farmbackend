from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from extensions import db

class Country(db.Model):
    __tablename__ = 'countries'

    id = Column(Integer, primary_key = True)
    name = Column(String, unique = True, nullable = False)

    # To store and manage information about countries.
    # Acts as a parent entity for related entities like Farmer and Farm.

    farmers = relationship("Farmer", back_populates = "country")
    farms = relationship("Farm", back_populates = "country")

    def __repr__(self):
        return f"<Country(id={self.id}, name={self.name})>"
    

# In SQLAlchemy, back_populates is used to establish a bidirectional relationship between two related models. 
# It allows both sides of a relationship to be aware of each other and access each other's related data seamlessly.


# farmers (Relationship) -> establishes a one-to-many relationship with the Farmer model
# back_populates="country" allows bi-directional relationship access
# You can access all farmers for a country using country.farmers
# Each farmer will have a reference to their country using farmer.country

# farms (Relationship) -> Establishes a one-to-many relationship with the Farm model
# Similar to farmers, this relationship is bi-directional
# Access all farms in a country using country.farms
# Each farm will have a reference to its country using farm.country

# __repr__
# Provides a readable string representation of the Country object
# Example -> country = Country(id=1, name="India")
# print(country)
# Output: <Country(id=1, name=India)>

