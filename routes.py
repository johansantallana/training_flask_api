from flask import jsonify, request
from services import create_gundam, get_all_gundams, get_gundam_by_id, delete_gundam_by_id, update_gundam_by_id, health_check, create_battle

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