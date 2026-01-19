from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Gundam(db.Model):
    __tablename__ = "gundams"
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)

