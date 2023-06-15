#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 17:32:39 2023

@author: ushnah.abbasi
"""

from flask import Flask, jsonify,request
from db_connect import db_connect

app = Flask(__name__)


@app.route('/usage', methods=['GET'])
def get_usage():
    timestamp = request.args.get('timestamp')
    #idd=request.args.get('idd')
    print(timestamp)
   
    query = f"SELECT * FROM memory_usage WHERE timestamp = {timestamp}"
    #query = f"SELECT * FROM dummy_data WHERE id = '{idd}'"
    print(query)
    conn=db_connect()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    cursor.close()
    return jsonify(data)


if __name__ == '__main__':
    app.run(port=2910)