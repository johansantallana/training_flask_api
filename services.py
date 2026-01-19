from  models import db, Gundam

def create_gundam(gundam):
    if gundam is None or not isinstance(gundam, dict):
        return {"error": "Invalid JSON"}, 400
    
    if "name" not in gundam:
        return {"error": "Field 'name' is required"}, 400

    name = gundam["name"]
    if not isinstance(name, str) or name.strip() == "":
        return {"error": "Field 'name' must be a non-empty string"}, 400
    
    new_gundam = Gundam(name = name.strip())

    db.session.add(new_gundam)
    db.session.commit()

    return {
        "gundam_id": new_gundam.id,
        "name": new_gundam.name
    }, 201

def get_all_gundams():
    gundams = Gundam.query.all()

    response = []
    for gundam in gundams:
        response.append({
            "gundam_id": gundam.id,
            "name": gundam.name
        })
    return response, 200

def get_gundam_by_id(id):
    gundam = Gundam.query.filter_by(id=id).first()
    if gundam is not None:
        return {
            "gundam_id": gundam.id,
            "name": gundam.name
        }, 200
    return {"error": "Gundam not found"}, 404

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

def find_max_id(data):
    max_id = 0
    for gundam in data:
        if gundam['gundam_id'] > max_id:
            max_id = gundam['gundam_id']
    return max_id