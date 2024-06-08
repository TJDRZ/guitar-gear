import os
from dotenv import load_dotenv
import psycopg2.extras

load_dotenv()

psycopg2.extras.register_uuid()

def connectDB():
    conn = psycopg2.connect(host = os.getenv("HOST"), dbname = os.getenv("DBNAME"), user = os.getenv("USER"), password = os.getenv("PASSWORD"), port = os.getenv("PORT"))
    cursor = conn.cursor()
    return {
        "conn": conn,
        "cursor": cursor
    }
