from flask import Blueprint, jsonify, request
from decorators import role_required, Role
from services.country_service import CountryService

country_blueprint = Blueprint('/country', __name__)

@country_blueprint.route('/all', methods=['GET'])
@role_required()
def getAllCountries():
    countries = CountryService.get_all_countries()
    return jsonify(countries), 200

@country_blueprint.route('/<int:id>', methods=['GET'])
@role_required()
def getCountryById(id):
    country = CountryService.get_country_by_id(id)
    print("Country", country)
    if country:
        return jsonify(country), 200
    return jsonify({"messaage": "Not Found"}), 404


@country_blueprint.route('/add-country', methods=['POST'])
@role_required([Role.ADMIN])
def addCountry():
    name = request.args.get('name')
    if not name:
        return jsonify({"message":"Name can not be empty"}), 400
    response, status = CountryService.add_country(name)
    return jsonify(response), status


@country_blueprint.route('/update-country/<int:id>', methods=['PUT'])
@role_required([Role.ADMIN])
def update_country(id):
    data = request.get_json()
    name = data.get('name')

    if not name:
        return jsonify({"message": "Name cannot be empty"}), 400

    response, status = CountryService.update_country_by_id(id, name)
    return jsonify(response), status



@country_blueprint.route('/delete-country/<int:id>', methods=['DELETE'])
@role_required([Role.ADMIN])
def delete_country(id):
    response, status = CountryService.delete_country_by_id(id)
    return jsonify(response), status