

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
    if timestamp is not None:
        query = f"SELECT * FROM memory_usage WHERE timestamp = '{timestamp}'"
    else:
        query = "SELECT * FROM memory_usage WHERE "
        conditions = []

        if hour is not None:
            conditions.append(f"hour = {hour}")
        if minute is not None and hour is None and second is None:
            conditions.append(f"minute = {minute}")
        if minute is not None and hour is None and second is not None:
            conditions.append(f"minute = {minute} and second = {second}")
        if minute is not None and hour is not None and second is None:
            conditions.append(f"hour = {hour} and minute = {minute}")
        if second is not None and hour is None and minute is None:
            conditions.append(f"second = {second}")

        query += " and ".join(conditions)

    return query

