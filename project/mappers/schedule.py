from models.schedule import Schedule
from dtos.schedule_dto import ScheduleDTO

class ScheduleMapper:
    @staticmethod
    def to_dto(schedule: Schedule) -> ScheduleDTO:
        # Converts a Schedule domain model into a ScheduleDTO.
        return ScheduleDTO(
            id = schedule.id,
            days_after_sowing = schedule.days_after_sowing,
            fertiliser = schedule.fertiliser,
            quantity = schedule.quantity,
            quantity_unit = schedule.quantity_unit,
            price_per_unit = schedule.price_per_unit,
            farm_id = schedule.farm_id
        )

    @staticmethod
    def to_model(schedule_dto: ScheduleDTO) -> Schedule:
        # Converts a ScheduleDTO back into a Schedule domain model.
        return Schedule(
            id = schedule_dto.id,
            days_after_sowing = schedule_dto.days_after_sowing,
            fertiliser = schedule_dto.fertiliser,
            quantity = schedule_dto.quantity,
            quantity_unit = schedule_dto.quantity_unit,
            price_per_unit = schedule_dto.price_per_unit,
            farm_id = schedule_dto.farm_id
        )
    

# The ScheduleMapper class serves the same purpose as other mappers, like FarmerMapper or FarmMapper, 
# but is specifically tailored for the Schedule model and ScheduleDTO.