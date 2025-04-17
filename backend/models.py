from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Recipes(db.Model):
    recipe_id = db.Column(db.Integer, primary_key=True)
    cuisine = db.Column(db.String, nullable=False)
    title = db.Column(db.String(80), nullable=False)
    rating = db.Column(db.Float(precision=1), nullable=False)
    prep_time = db.Column(db.Integer, nullable=True)
    cook_time = db.Column(db.Integer, nullable=True)
    total_time = db.Column(db.Integer, nullable=True)
    description = db.Column(db.Text,nullable=True)
    nutrients = db.Column(db.Text,nullable=True)
    serves = db.Column(db.String,nullable=True)