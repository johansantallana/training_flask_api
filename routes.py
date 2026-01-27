from flask import jsonify, request
from services import create_gundam, get_all_gundams, get_gundam_by_id, delete_gundam_by_id, update_gundam_by_id, health_check, create_battle, create_weapon, get_battle_by_id, get_battles, update_battles_by_id, delete_battle_by_id, update_weapon_by_id, delete_weapon_by_id

def register_routes(app):

    @app.route('/')
    def welcome():
        return ("Welcome to Gundam Seed API like study case...By Fr33d0m!!!")

    @app.route('/health')
    def api_health():
        result, status_code = health_check()
        return jsonify(result), status_code

    @app.route('/gundams', methods = ["GET"])
    def gundams():
        result, status_code = get_all_gundams()
        return jsonify(result), status_code

    @app.route('/gundams/<int:id>', methods = ["GET"])
    def gundam_by_id(id):
        result, status_code = get_gundam_by_id(id)
        return jsonify(result), status_code

    @app.route('/gundams', methods = ["POST"])
    def add_gundam():
        gundam = request.get_json()
        result, status_code = create_gundam(gundam)
        return jsonify(result), status_code 

    @app.route('/gundams/<int:id>', methods = ["DELETE"])
    def delete_gundam(id):
        result, status_code = delete_gundam_by_id(id)
        return jsonify(result), status_code

    @app.route('/gundams/<int:id>', methods = ["PUT"])
    def update_gundam(id):
        gundam = request.get_json()
        result, status_code = update_gundam_by_id(id, gundam)
        return jsonify(result), status_code
    
    @app.route('/gundams/<int:id>/battles', methods = ["POST"])
    def add_battle(id):
        body = request.get_json()
        result, status_code = create_battle(id, body)
        return jsonify(result), status_code
    
    @app.route('/battles/<int:id>/weapons', methods = ["POST"])
    def add_weapon(id):
        body = request.get_json()
        result, status_code = create_weapon(id, body)
        return jsonify(result), status_code

    @app.route('/battles/<int:id>', methods = ["GET"])
    def battle_by_id(id):
        result, status_code = get_battle_by_id(id)
        return jsonify(result), status_code
    
    @app.route('/battles', methods = ["GET"])
    def get_all_battles():
        result, status_code = get_battles()
        return jsonify(result), status_code
    
    @app.route('/battles/<int:id>', methods = ["PUT"])
    def update_battle(id):
        battle = request.get_json()
        result, status_code = update_battles_by_id(id, battle)
        return jsonify(result), status_code
    
    @app.route('/battles/<int:id>', methods = ["DELETE"])
    def delete_battle(id):
        result, status_code = delete_battle_by_id(id)
        return jsonify(result), status_code

    @app.route('/weapons/<int:id>', methods = ["PUT"])
    def update_weapon(id):
        body = request.get_json()
        result, status_code = update_weapon_by_id(id, body)
        return jsonify(result), status_code

    @app.route('/weapons/<int:id>', methods = ["DELETE"])
    def delete_weapon(id):
        result, status_code = delete_weapon_by_id(id)
        return jsonify(result), status_code