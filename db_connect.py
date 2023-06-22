#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 00:27:54 2023

@author: ushnah.abbasi
"""

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
