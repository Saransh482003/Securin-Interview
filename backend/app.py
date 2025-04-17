from backend import app, db
from flask import request, redirect, jsonify
import requests
from .insertDB import insertDB

# cache = Cache(app, config={
#     'CACHE_TYPE': 'RedisCache',
#     'CACHE_REDIS_HOST': 'localhost',
#     'CACHE_REDIS_PORT': 6379,
#     'CACHE_REDIS_DB': 0,
#     'CACHE_REDIS_URL': 'redis://localhost:6379/0'
# })



@app.route("/", methods=["GET"])
def index():
    return {"message":"Hello"}

# @app.route("/all-recipes", methods=["GET"])
# def all_recipes():
#     args = request.args.to_dict()
#     page = args["page"] if "page" in args else 1
#     limit = args["limit"] if "limit" in args else 10
#     url = f"http://127.0.0.1:5000/api/recipes?page={page}&limit={limit}"
#     return {"message":"Hello"}



@app.route("/admin/addrows", methods=["GET"])
def add_rows():
    args = request.args.to_dict()
    insertDB(args["file_name"])
    return {"message":"Rows Successfully Added"}


if __name__ == "__main__":
    app.run(debug=True)