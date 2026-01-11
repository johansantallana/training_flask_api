from flask import jsonify
from data import data
from services import build_summary

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

    @app.route('/gundams')
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



    