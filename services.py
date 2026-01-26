from  models import db, Gundam, Battle, Weapon

def health_check():
    total = Gundam.query.count()
    return {
        "status": "OK",
        "version": "1.0",
        "number_of_gundams": total
    }, 200

def get_all_gundams():
    gundams = Gundam.query.all()
    
    list_gundam = []
    for gundam in gundams:
        list_battle = []
        for battle in gundam.battles:
            list_weapon = []
            for weapon in battle.weapons:
                list_weapon.append({
                    "weapon_id": weapon.id,
                    "name": weapon.name,
                    "damage": weapon.damage
                })
            list_battle.append({
                "battle_id": battle.id,
                "name": battle.name,
                "weapons": list_weapon
            })
        list_gundam.append({
            "gundam_id": gundam.id,
            "name": gundam.name,
            "battles": list_battle
        })
    
    return list_gundam, 200

def get_gundam_by_id(id):
    gundam = Gundam.query.filter_by(id=id).first()
    if gundam is None:
        return {"error": "Gundam not found"}, 404
    
    battles = []
    for battle in gundam.battles:
        battles.append({
            "battle_id": battle.id,
            "name": battle.name
        })
    
    return {
        "gundam_id": id,
        "name": gundam.name,
        "battles": battles
        }, 200
    
def get_battle_by_id(id):
    battle = Battle.query.filter_by(id = id).first()
    if battle is None:
        return {"error": "Battle not found"}, 404
    
    weapons = []
    for weapon in battle.weapons:
        weapons.append({
            "weapon_id": weapon.id,
            "name": weapon.name,
            "damage": weapon.damage
        })
    return {
        "battle_id": id,
        "name": battle.name,
        "gundam_id": battle.gundam.id,
        "weapons": weapons
    }, 200
        

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

def delete_gundam_by_id(id):
    gundam = Gundam.query.filter_by(id=id).first()
    if gundam is None:
        return {"error": "Gundam not found"}, 404
    db.session.delete(gundam)
    db.session.commit()

    return {
        "message": "Gundam deleted succefully",
        "gundam_id": id
    }, 200

def update_gundam_by_id(id, body):
    gundam = Gundam.query.filter_by(id=id).first()
    if gundam is None:
        return {"error": "Gundam not found"}, 404
    if body is None or not isinstance(body, dict):
        return {"error": "Invalid JSON body"}, 400
    if "name" not in body:
        return {"error": "Field 'name' is required"}, 400

    name = body["name"]
    if not isinstance(name, str) or name.strip() == "":
        return {"error": "Field 'name' must be a non-empty string"}, 400

    gundam.name = name.strip()
    db.session.commit()
    return {
        "gundam_id": gundam.id,
        "name": gundam.name
    }, 200

def create_battle(id, body):
    if body is None or not isinstance(body, dict):
        return {"error": "Invalid JSON body"}, 400    
    if "name" not in body:
        return {"error": "Field name is required"}, 400
    name = body["name"]
    if not isinstance(name, str) or name.strip() == "":
        return {"error": "Flield 'Name' must be a non-empty string"}, 400
    gundam = Gundam.query.filter_by(id = id).first()
    if gundam is None:
        return {"error": "Gundam not found"}, 404
    
    battle = Battle(
        name = name.strip(),
        gundam_id = id
    )
    
    db.session.add(battle)
    db.session.commit()
    
    return {
        "battle_id": battle.id,
        "name": battle.name,
        "gundam_id": battle.gundam_id
    }, 201
    
def create_weapon(id, body):
    if body is None or not isinstance(body, dict):
        return {"error": "Invalid JSON body"}, 400
    if "name" not in body:
        return {"error": "Field 'name' is required"}, 400
    if "damage" not in body:
        return {"error": "Field 'damage' is required"}, 400
    name = body["name"]
    damage = body["damage"]
    
    if not isinstance(name, str) or name.strip() == "":
        return {"error": "Field 'name' must be a non-empty string"}, 400
    if not isinstance(damage, int) or damage < 0:
        return {"error": "Field 'damage' must be a positive integer"}, 400
    
    battle = Battle.query.filter_by(id=id).first()
    
    if battle is None:
        return {"error": "Battle not found"}, 404
    
    weapon = Weapon(
        name = name.strip(),
        damage = damage,
        battle_id = id
    )
    
    db.session.add(weapon)
    db.session.commit()
    
    return{
        "weapon_id": weapon.id,
        "name": weapon.name,
        "damage": weapon.damage,
        "battle_id": weapon.battle_id
    }, 201