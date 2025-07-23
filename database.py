from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

def connexion():

    db = mysql.connector.connect(
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD'),
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME')
    )
    return db
