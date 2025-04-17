from flask import Blueprint, jsonify
from flask_restful import Api, Resource, marshal_with, reqparse, fields, abort, request
from sqlalchemy.sql.expression import func, desc, case, exists, text
from backend.models import Recipes
import json
from backend.models import db

api_search = Blueprint("api_search",__name__)
api_s = Api(api_search)


class recipeSearch(Resource):
    def get(self):
        args = request.args.to_dict()
        arguments = {
            "calories" : args["calories"] if "calories" in args else None,
            "title" : args["title"] if "title" in args else None,
            "cuisine" : args["cuisine"] if "cuisine" in args else None,
            "total_time" : args["total_time"] if "total_time" in args else None,
            "rating" : args["rating"] if "rating" in args else None
        }
        query = f"SELECT * FROM Recipes WHERE title LIKE '%{arguments['title']}%' AND cuisine LIKE '%{arguments['cuisine']}%' AND total_time {arguments['total_time']} AND rating {arguments['rating']}"
        fetcher = db.session.execute(text(query))

        if fetcher:
            recipe_list = []
            for row in fetcher:
                nutrients = json.loads(row.nutrients)
                cal = int(nutrients["calories"].split(" ")[0])
                arg_cal = arguments["calories"]
                operators = [">=","<=",">","<","="]
                for op in operators:
                    if op in arg_cal:
                        arg_cal = int(arg_cal.replace(op,""))
                        break
                if eval(f"{cal} {op} {arg_cal}"):
                    recipe_list.append({
                        "recipe_id":row[0],
                        "cuisine":row[1],
                        "title":row[2],
                        "rating":row[3],
                        "prep_time":row[4],
                        "cook_time":row[5],
                        "total_time":row[6],
                        "description":row[7],
                        "nutrients":json.loads(row[8]),
                        "serves":row[9],
                    })
            
            return recipe_list, 200
        abort(400, message= "No data exists")


api_s.add_resource(recipeSearch,"/")