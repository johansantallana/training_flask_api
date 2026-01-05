from flask import Flask, request, jsonify

app = Flask(__name__)

gundam = {
  "api": {
    "name": "gundam-seed-destiny-api",
    "version": "1.0",
    "endpoint": "/v1/series/gundam-seed-destiny/characters?limit=5"
  },
  "data": [
    {
      "id": "shinn-asuka",
      "name": "Shinn Asuka",
      "affiliation": "ZAFT",
      "role": "Protagonist",
      "mobileSuits": ["ZGMF-X56S Impulse Gundam", "ZGMF-X42S Destiny Gundam"]
    },
    {
      "id": "kira-yamato",
      "name": "Kira Yamato",
      "affiliation": "Three Ships Alliance",
      "role": "Main Character",
      "mobileSuits": ["ZGMF-X20A Strike Freedom Gundam"]
    },
    {
      "id": "athrun-zala",
      "name": "Athrun Zala",
      "affiliation": "Orb / Three Ships Alliance",
      "role": "Main Character",
      "mobileSuits": ["ZGMF-X09A Justice Gundam", "ZGMF-X19A Infinite Justice Gundam"]
    },
    {
      "id": "cagalli-yula-athha",
      "name": "Cagalli Yula Athha",
      "affiliation": "Orb Union",
      "role": "Main Character",
      "mobileSuits": ["MBF-02 Strike Rouge"]
    },
    {
      "id": "lacus-clyne",
      "name": "Lacus Clyne",
      "affiliation": "Three Ships Alliance",
      "role": "Main Character",
      "mobileSuits": []
    }
  ],
  "meta": {
    "count": 5,
    "series": "Mobile Suit Gundam SEED Destiny",
    "language": "en"
  }
}


@app.route('/')
def home():
    return "ok"

@app.route('/users')
def list_characters():
    return gundam

@app.route('/users', methods=["POST"])
def add_character():
    gundam["data"].append(request.get_json())
    gundam["meta"]["count"] = gundam["meta"]["count"] + 1
    return "Gundam insertado con exito", 201

app.run(host='0.0.0.0', port='5000', debug=True)