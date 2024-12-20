from flask import Blueprint, jsonify, request
from services.schedule_service import ScheduleService
from decorators import Role, role_required

schedule_blueprint = Blueprint('schedule', __name__)

@schedule_blueprint.route('/today', methods=['GET'])
@role_required([Role.VIEWER])
def get_schedules_due_for_today():
    try:
        schedules = ScheduleService.get_schedules_due_for_today()
        return jsonify(schedules), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@schedule_blueprint.route('/tomorrow', methods=['GET'])
@role_required()
def get_schedules_due_for_tomorrow():
    try:
        schedules = ScheduleService.get_schedules_due_for_tomorrow()
        return jsonify(schedules), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@schedule_blueprint.route('/all', methods=['GET'])
@role_required()
def allSchedules():
    try:
        schedules = ScheduleService.get_all_schedules()
        if schedules:
            return jsonify(schedules), 200
        return jsonify({"message": "No schedules found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    

@schedule_blueprint.route('/create-schedule', methods=['POST'])
@role_required([Role.ADMIN])
def create_schedule():
    try:
        data = request.get_json()
        schedule = ScheduleService.create_schedule(data['days_after_sowing'], data['fertiliser'], data['quantity'], data['quantity_unit'], data['price_per_unit'], data['farm_id'])
        return jsonify(schedule), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


    
@schedule_blueprint.route('/update/<int:id>', methods=['PUT'])
@role_required([Role.ADMIN])
def update_schedule(id):
    try:
        data = request.get_json()
        days_after_sowing = data.get('days_after_sowing')
        fertiliser = data.get('fertiliser')
        quantity = data.get('quantity')
        quantity_unit = data.get('quantity_unit')
        price_per_unit = data.get('price_per_unit')
        farm_id = data.get('farm_id')

        if not (days_after_sowing and fertiliser and quantity and quantity_unit and price_per_unit and farm_id):
            return jsonify({"message": "All fields are required"}), 400

        response, status = ScheduleService.update_schedule_by_id(id, days_after_sowing, fertiliser, quantity, quantity_unit, price_per_unit, farm_id)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@schedule_blueprint.route('/delete/<int:id>', methods=['DELETE'])
@role_required([Role.ADMIN])
def delete_schedule(id):
    try:
        response, status = ScheduleService.delete_schedule_by_id(id)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500
