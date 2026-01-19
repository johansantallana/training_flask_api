from flask import Flask
from routes import register_routes
from models import db

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gundams.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
with app.app_context():
    db.create_all()

register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)