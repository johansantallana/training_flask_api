from flask import jsonify, request
from data import data
from services import build_summary, find_max_id

def register_routes(app):

    @app.route('/')
    def welcome():
        return ("Welcome to Gundam Seed API like study case...By Fr33d0m!!!")

    @app.route('/health')
    def api_health():
        json_output = {
            "status" : "OK",
            "version" : "1.0",
            "number_of_gundams" : len(data)
        }
        return jsonify(json_output)

    @app.route('/gundams', methods = ["GET"])
    def gundams():
        return jsonify(data)

    @app.route('/gundams/summary', methods = ["GET"])
    def gundams_summary():
        return jsonify(build_summary(data)), 200

    @app.route('/gundams/<int:id>/summary', methods = ["GET"])
    def gundam_summary(id):
        for gundam in data:
            if gundam["gundam_id"] == id:
                return jsonify(build_summary([gundam])[0]), 200
        return {"error": "Gundam not found"}, 404

    @app.route('/gundams/<int:id>', methods = ["GET"])
    def single_gundam(id):
        for gundam in data:
            if gundam["gundam_id"] == id:
                return jsonify(gundam), 200
        return {"error": "Gundam not found"}, 404

    @app.route('/gundams', methods = ["POST"])
    def add_gundam():
        gundam = request.get_json()

        if gundam is None:
            return jsonify({'error': 'Body must be valid JSON'}), 400
        
        if "name" not in gundam:
            return jsonify({'error': 'Missing required field "name"'}), 400
        
        if not isinstance(gundam['name'], str) or gundam['name'].strip() == "":
            return jsonify({"error": '"name" must be a non-empty string'}), 400

        if 'battles' not in gundam:
            gundam['battles'] = []

        if not isinstance(gundam['battles'], list):
            return jsonify({"error": '"battles" must be a list'}), 400
        
        new_id = find_max_id(data) + 1

        new_gundam = {
        "gundam_id": new_id,
        "name": gundam["name"],
        "battles": gundam["battles"]
        }

        data.append(new_gundam)
        return jsonify(new_gundam), 201