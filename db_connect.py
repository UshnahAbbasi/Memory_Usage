

import psycopg2
from psycopg2.extras import RealDictCursor
import os
from dotenv import load_dotenv


# loading from .env file
load_dotenv()

db_user=os.getenv('DB_USER')
db_password=os.getenv('DB_password')



def db_connect():
    conn = psycopg2.connect(
        host='localhost',
        port='5432',
        database='db_ushnah',
        user=db_user,
        password=db_password
        )
    return conn

def get_data(query):
    conn=db_connect()
    cursor = conn.cursor()
    cursor.execute(query)
    data = cursor.fetchall()
    print(data)
    cursor.close()
    return data

def get_query(timestamp, hour, minute, second):
    if timestamp != None:
        query = f"SELECT * FROM memory_usage WHERE timestamp = '{timestamp}'"
    else:
        if hour != None:
            query = f"SELECT * FROM memory_usage WHERE hour = {hour}"
        if minute != None:
            query = f"SELECT * FROM memory_usage WHERE hour = {hour} and minute ={minute}"
        if second != None:
            query = f"SELECT * FROM memory_usage WHERE hour = {hour} and minute ={minute} and second={second} "
    
    return query
