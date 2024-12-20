from repositories.schedule_repo import ScheduleRepository

class ScheduleService:

    @staticmethod
    def get_schedules_due_for_today():
        try:
            schedules = ScheduleRepository.get_schedules_due_for_today()
            return [s.as_dict() for s in schedules]        # Return the list of DTOs as dictionaries
        except Exception as e:
            raise e

    @staticmethod
    def get_schedules_due_for_tomorrow():
        try:
            schedules = ScheduleRepository.get_schedules_due_for_tomorrow()
            return [s.as_dict() for s in schedules]       # Return the list of DTOs as dictionaries
        except Exception as e:
            raise e
        
    @staticmethod
    def get_all_schedules():
        try:
            schedules = ScheduleRepository.get_all_schedules()
            return [s.as_dict() for s in schedules] if schedules else None  # Return the list of DTOs as dictionaries
        except Exception as e:
            raise e

    @staticmethod
    def create_schedule(days_after_sowing, fertiliser, quantity, quantity_unit, price_per_unit, farm_id):
        try:
            schedule = ScheduleRepository.create_schedule(days_after_sowing, fertiliser, quantity, quantity_unit, price_per_unit, farm_id)
            return schedule.as_dict()         # Return the DTO as a dictionary
        except Exception as e:
            raise e


    @staticmethod
    def update_schedule_by_id(id, days_after_sowing, fertiliser, quantity, quantity_unit, price_per_unit, farm_id):
        try:
            schedule, error = ScheduleRepository.update_schedule_by_id(id, days_after_sowing, fertiliser, quantity, quantity_unit, price_per_unit, farm_id)
            if error:
                return {"error": error}, 400

            return schedule.as_dict(), 200  # Return the DTO as a dictionary
        except Exception as e:
            return {"error": str(e)}, 500


    @staticmethod
    def delete_schedule_by_id(id):
        try:
            response, status = ScheduleRepository.delete_schedule_by_id(id)
            return response, status
        except Exception as e:
            return {"error": str(e)}, 500