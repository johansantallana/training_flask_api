from flask import Flask, request, jsonify

app = Flask(__name__)

gundam = {
    "api": {
        "name": "gundam-seed-destiny-api",
        "version": "1.0.0",
        "status": "stable",
        "baseUrl": "https://api.example.com",
        "documentation": "https://api.example.com/docs"
    },

    "data": [
        {
            "id": "shinn-asuka",
            "type": "character",
            "attributes": {
                "name": "Shinn Asuka",
                "affiliation": "ZAFT",
                "role": "Protagonist"
            },
            "relationships": {
                "mobileSuits": [
                    "ZGMF-X56S Impulse Gundam",
                    "ZGMF-X42S Destiny Gundam"
                ]
            }
        },
        {
            "id": "kira-yamato",
            "type": "character",
            "attributes": {
                "name": "Kira Yamato",
                "affiliation": "Three Ships Alliance",
                "role": "Main Character"
            },
            "relationships": {
                "mobileSuits": [
                    "ZGMF-X20A Strike Freedom Gundam"
                ]
            }
        },
        {
            "id": "cagalli-yula-athha",
            "type": "character",
            "attributes": {
                "name": "Cagalli Yula Athha",
                "affiliation": "Orb Union",
                "role": "Main Character"
            },
            "relationships": {
                "mobileSuits": [
                    "MBF-02 Strike Rouge"
                ]
            }
        },
        {
            "id": "mu-la-flaga",
            "type": "character",
            "attributes": {
                "name": "Mu La Flaga",
                "affiliation": "Earth Alliance / Orb",
                "role": "Ace Pilot"
            },
            "relationships": {
                "mobileSuits": [
                    "TS-MA2mod.00 Moebius Zero",
                    "GAT-105 Strike Gundam (support)"
                ]
            }
        }
    ],

    "meta": {
        "count": 4,
        "total": 5,
        "series": {
            "id": "gundam-seed-destiny",
            "name": "Mobile Suit Gundam SEED Destiny",
            "language": "en"
        }
    }
}



@app.route('/')
def home():
    return "ok"

@app.route('/users')
def list_characters():
    return gundam

@app.route('/users', methods=["POST"])
def add_gundam():
    gundam["data"].append(request.get_json())
    gundam["meta"]["count"] = len(gundam["data"])
    return "Gundam insertado con exito", 201

@app.route('/users/<string:id>', methods=["DELETE"])
def delete_gundam(id):

    for gundam_item in gundam["data"]:
        if gundam_item["id"] == id:
            gundam["data"].remove(gundam_item)
            gundam["meta"]["count"] = len(gundam["data"])
            return "Gundam Eliminado Correctamente", 200

    return "Gundam no encontrado o id incorrecto", 404

@app.route('/users/<string:id>', methods=["PATCH"])
def update_gundam(id):
    body = request.get_json()

    for gundam_item in gundam["data"]:
        if gundam_item["id"] == id:
            gundam_item["name"] = body["name"]
            return "Gundam actualizado correctamente", 200

    return "Gundam no encontrado o id incorrecto", 404

app.run(host='0.0.0.0', port='5000', debug=True)