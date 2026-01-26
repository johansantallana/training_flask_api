from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Gundam(db.Model):
    __tablename__ = "gundams"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)

    battles = db.relationship(
        "Battle",
        back_populates = "gundam",
        cascade = "all, delete-orphan"
    )

class Battle(db.Model):
    __tablename__ = "battles"
    
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    gundam_id = db.Column(db.Integer, db.ForeignKey("gundams.id"), nullable = False)
    
    gundam = db.relationship("Gundam", back_populates = "battles")

    weapons = db.relationship(
        "Weapon",
        back_populates = "battle",
        cascade = "all, delete-orphan"
    )

class Weapon(db.Model):
    __tablename__ = "weapons"

    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100), nullable = False)
    damage = db.Column(db.Integer, nullable = False)
    battle_id = db.Column(db.Integer, db.ForeignKey("battles.id"), nullable = False)

    battle = db.relationship("Battle", back_populates = "weapons")