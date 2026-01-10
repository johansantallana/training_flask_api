from flask import Flask, jsonify
app = Flask(__name__)

data = [
    {
        "gundam_id": 1,
        "name": "Strike Gundam",
        "battles": [
            {
                "battle_id": 101,
                "weapons": [
                    {"weapon_id": 1001, "name": "Beam Rifle", "damage": 120},
                    {"weapon_id": 1002, "name": "Shield Bash", "damage": 40}
                ]
            },
            {
                "battle_id": 102,
                "weapons": [
                    {"weapon_id": 1003, "name": "Armor Schneider", "damage": 60}
                ]
            }
        ]
    },
    {
        "gundam_id": 2,
        "name": "Aegis Gundam",
        "battles": [
            {
                "battle_id": 103,
                "weapons": [
                    {"weapon_id": 1004, "name": "Beam Sabers", "damage": 110},
                    {"weapon_id": 1005, "name": "Claw System", "damage": 90}
                ]
            }
        ]
    },
    {
        "gundam_id": 3,
        "name": "Buster Gundam",
        "battles": [
            {
                "battle_id": 104,
                "weapons": [
                    {"weapon_id": 1006, "name": "High-Energy Rifle", "damage": 180}
                ]
            },
            {
                "battle_id": 105,
                "weapons": [
                    {"weapon_id": 1007, "name": "Missile Launcher", "damage": 150}
                ]
            }
        ]
    },
    {
        "gundam_id": 4,
        "name": "Duel Gundam",
        "battles": [
            {
                "battle_id": 106,
                "weapons": [
                    {"weapon_id": 1008, "name": "Beam Saber", "damage": 100},
                    {"weapon_id": 1009, "name": "Assault Shroud Cannon", "damage": 140}
                ]
            }
        ]
    },
    {
        "gundam_id": 5,
        "name": "Blitz Gundam",
        "battles": [
            {
                "battle_id": 107,
                "weapons": [
                    {"weapon_id": 1010, "name": "Gleipnir Claw", "damage": 130},
                    {"weapon_id": 1011, "name": "Lancer Dart", "damage": 80}
                ]
            }
        ]
    },
    {
        "gundam_id": 6,
        "name": "Justice Gundam",
        "battles": [
            {
                "battle_id": 108,
                "weapons": [
                    {"weapon_id": 1012, "name": "Fatum-00 Beam Cannons", "damage": 160},
                    {"weapon_id": 1013, "name": "Beam Saber", "damage": 120}
                ]
            },
            {
                "battle_id": 109,
                "weapons": [
                    {"weapon_id": 1014, "name": "Beam Rifle", "damage": 140}
                ]
            }
        ]
    }
]


def build_summary(data):
    response = []

    for gundam in data:
        total_damage = 0
        total_weapons = 0
        most_powerful_weapon_name = ""
        most_powerful_weapon_damage = 0

        for battle in gundam["battles"]:
            for weapon in battle["weapons"]:
                total_damage += weapon["damage"]
                total_weapons += 1

                if weapon["damage"] > most_powerful_weapon_damage:
                    most_powerful_weapon_damage = weapon["damage"]
                    most_powerful_weapon_name = weapon["name"]

        temp = {
            "gundam": gundam["name"],
            "total_damage": total_damage,
            "total_weapons_used": total_weapons,
            "most_powerful_weapon": {
                "name": most_powerful_weapon_name,
                "damage": most_powerful_weapon_damage
            }
        }

        response.append(temp)

    return response

@app.route('/')
def welcome():
    return ("Welcome to Gundam Seed API like study case...By Fr33d0m!!!")

@app.route('/gundams')
def gundams():
    return jsonify(data)

@app.route('/gundams/summary', methods = ["GET"])
def gundams_summary():
    return jsonify(build_summary(data)), 200

@app.route('/gundam/<int:id>/summary', methods = ["GET"])
def gundam_summary(id):
    for gundam in data:
        if gundam["gundam_id"] == id:
            temp = [gundam]
            return jsonify(build_summary(temp)[0]), 200
    return {"error": "Gundam not found"}, 404

if __name__ == "__main__":
    app.run(debug=True)