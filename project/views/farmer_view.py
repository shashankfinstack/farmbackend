from flask import Blueprint, jsonify, request
from services.farmer_service import FarmerService
from decorators import role_required, Role

farmer_blueprint = Blueprint('farmer', __name__)

@farmer_blueprint.route('/allfarmers', methods=['GET'])
@role_required()
def allFarmers():
    try:
        page = request.args.get('page', 1, type=int)                              # PAGINATION
        page_size = request.args.get('pageSize', 10, type=int)
        
        farmers, total_count = FarmerService.get_all_farmers(page, page_size)
        return jsonify({
            'farmers': [f.as_dict() for f in farmers],
            'totalCount': total_count
        }), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@farmer_blueprint.route('/<int:id>', methods=['GET'])
@role_required()
def getFarmer(id):
    try:
        farmer = FarmerService.get_farmer_by_id(id)
        if farmer:
            return jsonify(farmer), 200
        return jsonify({"error": "Farmer not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@farmer_blueprint.route('/create-farmer', methods=['POST'])
@role_required([Role.ADMIN])
def createFarmer():
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    required_fields = ['phone_number', 'name', 'language', 'country_id']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    response, status = FarmerService.create_farmer(data['phone_number'], data['name'], data['language'], data['country_id'])
    return jsonify(response), status


@farmer_blueprint.route('/crop/<crop>', methods=['GET'])
@role_required()
def getFarmersByCropGrown(crop):
    if not crop:
        return jsonify({"message": "Crop name is empty"}), 400
    try:
        farmers = FarmerService.get_farmers_by_crop(crop)
        return jsonify(farmers), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500



@farmer_blueprint.route('/calculate_bill', methods=['POST'])
@role_required()
def calculate_bill():
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    fertilizer_name = data.get('fertilizer')
    quantity = data.get('quantity')

    if not fertilizer_name or not quantity:
        return jsonify({"error": "Fertilizer name and quantity are required"}), 400

    try:
        total_cost = FarmerService.calculate_bill(fertilizer_name, quantity)
        return jsonify({"total_cost": total_cost}), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
    
@farmer_blueprint.route('/<int:farmer_id>/bill_of_materials', methods=['GET'])
@role_required()
def get_bill_of_materials(farmer_id):
    try:
        total_cost = FarmerService.calculate_bill_of_materials(farmer_id)
        return jsonify({"farmer_id": farmer_id, "total_cost": total_cost}), 200
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500


    
@farmer_blueprint.route('/update-farmer/<int:id>', methods=['PUT'])
@role_required([Role.ADMIN])
def update_farmer(id):
    data = request.json
    if not data:
        return jsonify({"error": "Invalid input"}), 400

    required_fields = ['phone_number', 'name', 'language', 'country_id']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"{field} is required"}), 400

    response, status = FarmerService.update_farmer_by_id(id, data['phone_number'], data['name'], data['language'], data['country_id'])
    return jsonify(response), status



@farmer_blueprint.route('/delete-farmer/<int:id>', methods=['DELETE'])
@role_required([Role.ADMIN])
def delete_farmer(id):
    try:
        response, status = FarmerService.delete_farmer_by_id(id)
        return jsonify(response), status
    except Exception as e:
        return jsonify({"error": str(e)}), 500