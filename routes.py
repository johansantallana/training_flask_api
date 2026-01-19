from flask import jsonify, request
from data import data
from services import build_summary, find_max_id, create_gundam, get_all_gundams, get_gundam_by_id

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
        result, status_code = get_all_gundams()
        return jsonify(result), status_code

    @app.route('/gundams/summary', methods = ["GET"])
    def gundams_summary():
        return jsonify(build_summary(data)), 200

    @app.route('/gundams/<int:id>/summary', methods = ["GET"])
    def gundam_summary(id):
        result, status_code = get_gundam_by_id(id)
        return jsonify(result), status_code

    @app.route('/gundams/<int:id>', methods = ["GET"])
    def single_gundam(id):
        for gundam in data:
            if gundam["gundam_id"] == id:
                return jsonify(gundam), 200
        return {"error": "Gundam not found"}, 404

    @app.route('/gundams', methods = ["POST"])
    def add_gundam():
        gundam = request.get_json()
        result, status_code = create_gundam(gundam)
        return jsonify(result), status_code 

    @app.route('/gundams/<int:id>', methods = ["DELETE"])
    def delete_gundam(id):
        for gundam in data:
            if gundam['gundam_id'] == id:
                data.remove(gundam)
                return jsonify({"message": "Gundam Deleted", "gundam_id":id}), 200

        return jsonify({"error": "Gundam not found"}), 404

    @app.route('/gundams/<int:id>', methods = ["PUT"])
    def update_gundam(id):
        info = request.get_json()
        if info is None:
            return jsonify({'error': 'Body must be valid JSON'}), 400
        for gundam in data:
            if gundam["gundam_id"] == id:
                if 'name' in info:
                    if not isinstance(info["name"], str) or info["name"].strip() == "":
                        return jsonify({"error": '"name" must be a non-empty string'}), 400
                    gundam["name"] = info["name"]
                
                if 'battles' in info:
                    if not isinstance(info["battles"], list):
                        return jsonify({"error":"battles must be a list"}), 400
                    gundam["battles"] = info["battles"]

                return jsonify(gundam), 200

        return jsonify({"error": "Gundam not found"}), 404 