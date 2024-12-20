from flask import Blueprint, jsonify, request
from decorators import Role, role_required
from services.farm_service import FarmService
import traceback

farm_blueprint = Blueprint('farm', __name__)

@farm_blueprint.route('/allfarms', methods=['GET'])
@role_required()
def get_all_farms():
    try:
        farms = FarmService.get_all_farms()
        return jsonify(farms), 200
    except Exception as e:
        print ("".join(traceback.format_exception(
                type(e), e, e.__traceback__)))
        return jsonify({"error": str(e)}), 500

@farm_blueprint.route('/<int:farm_id>', methods=['GET'])
@role_required()
def get_farm_by_id(farm_id):
    try:
        farm = FarmService.get_farm_by_id(farm_id)
        return jsonify(farm) if farm else ('Not Found', 404)
    except Exception as e:
        print (e)
        return jsonify({"error": str(e)}), 500
    

@farm_blueprint.route('/create-farm', methods=['POST'])
@role_required([Role.ADMIN])
def create_farm():
    data = request.get_json()
    required_fields = ['area', 'village', 'crop_grown', 'sowing_date', 'farmer_id', 'country_id']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    try:
        response, status = FarmService.create_farm(
            data['area'], data['village'], data['crop_grown'], 
            data['sowing_date'], data['farmer_id'], data['country_id']
        )
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@farm_blueprint.route('/<int:farmer_id>/farms', methods=['GET'])
@role_required()
def get_farms_by_farmer_id(farmer_id):
    try:
        farms = FarmService.get_farms_by_farmer_id(farmer_id)
        return jsonify(farms), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
@farm_blueprint.route('/update-farm/<int:farm_id>', methods=['PUT'])
@role_required([Role.ADMIN])
def update_farm(farm_id):
    data = request.get_json()
    required_fields = ['area', 'village', 'crop_grown', 'sowing_date', 'farmer_id', 'country_id']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    try:
        response, status = FarmService.update_farm_by_id(
            farm_id, data['area'], data['village'], data['crop_grown'], 
            data['sowing_date'], data['farmer_id'], data['country_id']
        )
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@farm_blueprint.route('/delete-farm/<int:farm_id>', methods=['DELETE'])
@role_required([Role.ADMIN])
def delete_farm(farm_id):
    try:
        response, status = FarmService.delete_farm_by_id(farm_id)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500