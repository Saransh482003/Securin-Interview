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
        sub_qs = []
        if arguments["title"] != None:
            sub_qs.append(f" title LIKE '%{arguments['title']}%' ")
        if arguments["cuisine"] != None:
            sub_qs.append(f" cuisine LIKE '%{arguments['cuisine']}%' ")
        if arguments["total_time"] != None:
            sub_qs.append(f" total_time {arguments['total_time']} ")
        if arguments["rating"] != None:
            sub_qs.append(f" rating {arguments['rating']} ")

        query = f"SELECT * FROM Recipes WHERE"
        query += sub_qs[0]
        for i in sub_qs[1:]: query += f" AND {i}"
        fetcher = db.session.execute(text(query))

        if fetcher:
            if "calories" in list(args.keys()):
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
                    if op == "=": op = "=="
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
            else:
                recipe_list = []
                for row in fetcher:
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