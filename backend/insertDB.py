from .models import *
import sqlite3
import pandas as pd
import json

def insertDB(file_name):
    data = pd.read_json(file_name, orient="index")
    data.fillna("NULL", inplace=True)
    conn = sqlite3.connect("instance/recipes.sqlite3")
    cursor = conn.cursor()
    for i in range(len(data)):
        row = data.iloc[i]
        cursor.execute(f"""
            INSERT INTO Recipes (recipe_id, cuisine, title, rating, prep_time, cook_time, total_time, description, nutrients, serves) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (i, row['cuisine'], row['title'], row['rating'], row['prep_time'], row['cook_time'], row['total_time'], row['description'], json.dumps(row['nutrients']), row['serves']))
    conn.commit()
    conn.close()
