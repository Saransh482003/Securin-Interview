from flask import Blueprint, jsonify
from flask_restful import Api, Resource, marshal_with, reqparse, fields, abort, request
from sqlalchemy.sql.expression import func, desc, case, exists
from backend.models import Recipes
import json

api_recipie = Blueprint("api_recipie",__name__)
api_r = Api(api_recipie)


class recipieAll(Resource):
    def get(self):
        args = request.args.to_dict()
        page = int(args["page"]) if "page" in args else 1
        limit = int(args["limit"]) if "limit" in args else 10
        offset = limit*(page-1)
        
        fetcher = Recipes.query.filter(Recipes.rating != "NULL").order_by(desc(Recipes.rating)).offset(offset).limit(limit).all()
        if fetcher:
            recipe_list = []
            for recipe in fetcher:
                recipe_list.append({
                    "recipe_id":recipe.recipe_id,
                    "cuisine":recipe.cuisine,
                    "title":recipe.title,
                    "rating":recipe.rating,
                    "prep_time":recipe.prep_time,
                    "cook_time":recipe.cook_time,
                    "total_time":recipe.total_time,
                    "description":recipe.description,
                    "nutrients":json.loads(recipe.nutrients),
                    "serves":recipe.serves,
                })
            return recipe_list, 200
        abort(400, message= "No data exists")


api_r.add_resource(recipieAll,"/")