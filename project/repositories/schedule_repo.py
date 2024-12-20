from datetime import datetime, timedelta
from sqlalchemy import text, func
from extensions import db
from models.schedule import Schedule
from models.farms import Farm
from mappers.schedule import ScheduleMapper

class ScheduleRepository:
    # GET 
    @staticmethod
    def get_all_schedules():
        try:
            schedules = Schedule.query.all()
            return [ScheduleMapper.to_dto(s) for s in schedules]
        except Exception as e:
            raise e
        
    @staticmethod
    def get_schedules_by_date(target_date):
        "Retrieve schedules due for a specific date."
        try:
            schedules = (
                db.session.query(Schedule)
                .join(Farm)
                .filter(
                    func.DATE(
                        Farm.sowing_date
                        + text("INTERVAL '1 day' * schedules.days_after_sowing")
                    )
                    == target_date
                )
                .all()
            )
            # print(schedules)
            # breakpoint()
            return [ScheduleMapper.to_dto(s) for s in schedules]
        except Exception as e:
            raise e

    @staticmethod
    def get_schedules_due_for_today():
        return ScheduleRepository.get_schedules_by_date(datetime.today().date())
    

    @staticmethod
    def get_schedules_due_for_tomorrow():
        return ScheduleRepository.get_schedules_by_date(datetime.today().date() + timedelta(days=1))
    
    @staticmethod
    def get_schedule_by_fertiliser(fertiliser_name):
        try:
            schedule = Schedule.query.filter_by(fertiliser=fertiliser_name).first()
            return ScheduleMapper.to_dto(schedule) if schedule else None
        except Exception as e:
            raise e
        
    # CREATE 
    @staticmethod
    def create_schedule(days_after_sowing, fertiliser, quantity, quantity_unit, price_per_unit, farm_id):
        try:
            schedule = Schedule(
                days_after_sowing=days_after_sowing,
                fertiliser=fertiliser,
                quantity=quantity,
                quantity_unit=quantity_unit,
                price_per_unit=price_per_unit,
                farm_id=farm_id,
            )
            db.session.add(schedule)
            db.session.commit()
            return ScheduleMapper.to_dto(schedule)
        except Exception as e:
            raise e
        
    # UPDATE 
    @staticmethod
    def update_schedule_by_id(id, **kwargs):
        try:
            schedule = Schedule.query.get(id)
            if not schedule:
                return None, "Schedule not found"

            for key, value in kwargs.items():
                setattr(schedule, key, value)

            db.session.commit()
            return ScheduleMapper.to_dto(schedule), None
        except Exception as e:
            db.session.rollback()
            raise e
        
    # DELETE
    @staticmethod
    def delete_schedule_by_id(id):
        try:
            schedule = Schedule.query.get(id)
            if not schedule:
                return {"message": "Schedule not found"}, 404

            db.session.delete(schedule)
            db.session.commit()
            return {"message": "Schedule deleted successfully"}, 200
        except Exception as e:
            db.session.rollback()
            raise e
