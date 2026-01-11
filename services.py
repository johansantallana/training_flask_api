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