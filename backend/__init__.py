from flask import Flask
from flask_cors import CORS
from flask_caching import Cache
from .models import db
from .api.recipieAPI import api_recipie

# Flask Initialisation
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///recipes.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()

db.init_app(app)
CORS(app)

app.register_blueprint(api_recipie, url_prefix="/api/recipes")