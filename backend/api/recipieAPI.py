from flask import Blueprint, jsonify
from flask_restful import Api, Resource, marshal_with, reqparse, fields, abort, request
from backend.models import Recipes

api_recipie = Blueprint("api_recipie",__name__)
api_ad = Api(api_recipie)

returner = {
    "recipe_id":fields.Integer,
    "cuisine":fields.String,
    "title":fields.String,
    "rating":fields.Float,
    "prep_time":fields.Integer,
    "cook_time":fields.Integer,
    "total_time":fields.Integer,
    "description":fields.String,
    "nutrients":fields.String,
    "serves":fields.String,
}

class recipieAll(Resource):
    @marshal_with(returner)
    def get(self):
        print("ret")
        print(Recipes)
        data = Recipes.query.all()
        if data:
            return data, 200
        abort(400, message= "No data exists")


api_ad.add_resource(recipieAll,"/")