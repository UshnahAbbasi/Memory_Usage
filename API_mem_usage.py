#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 17:32:39 2023

@author: ushnah.abbasi
"""

from flask import Flask, jsonify,request
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

conn = psycopg2.connect(
    host='localhost',
    port='5432',
    database='db_ushnah',
    user='ushnah',
    password='abbasi'
    )


# ... Code to set up database connection and other configurations ...
@app.route('/usage', methods=['GET'])
def get_usage():
    timestamp = request.args.get('timestamp')
    #idd=request.args.get('idd')
    print(timestamp)
    # Perform a database query to retrieve the usage at the provided timestamp
    # You can adjust the query based on the structure of your 'dummy_data' table
    query = f"SELECT * FROM memory_usage WHERE timestamp = {timestamp}"
    #query = f"SELECT * FROM dummy_data WHERE id = '{idd}'"
    print(query)
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    cursor.close()
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=2910)