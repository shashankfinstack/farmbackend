from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship
from extensions import db

class Schedule(db.Model):
    __tablename__ = 'schedules'

    id = Column(Integer, primary_key=True)
    days_after_sowing = Column(Integer, nullable=False)
    fertiliser = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False)
    quantity_unit = Column(String, nullable=False)
    price_per_unit = Column(Float, nullable=False)   
    farm_id = Column(Integer, ForeignKey('farms.id'))

    farm = relationship("Farm", back_populates="schedules")

    def __repr__(self):
        return f"<Schedule(id={self.id}, fertiliser={self.fertiliser}, days_after_sowing={self.days_after_sowing})>"

# This model represents a schedule in the database. It stores information about fertilization and other farm activities based on the number of days after the crop was sown
# farm_id (Integer, ForeignKey)
# Foreign key linking the schedule to a specific farm (farms.id)
# establishes a relationship between the Schedule and Farm models

# __repr__ -> provides a readable string representation of the Schedule object
# schedule = Schedule(id=1, fertiliser="Urea", days_after_sowing=30)
# print(schedule)
# Output: <Schedule(id=1, fertiliser=Urea, days_after_sowing=30)>


# relationship("Farm", back_populates="schedules") establishes a connection between the Schedule and Farm classes.
# The farm attribute in Schedule provides access to the related Farm object.
# The schedules attribute in Farm provides access to all related Schedule objects.
# back_populates ensures bidirectional updates, maintaining consistency between the two related objects.