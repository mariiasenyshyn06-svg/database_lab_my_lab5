from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .root import register_routes
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    register_routes(app)
    create_tables(app)
    populate_data()
    return app

def create_tables(app):
    with app.app_context():
        db.create_all()

def populate_data():
    sql_file_path = os.path.abspath('data.sql')
    if os.path.exists(sql_file_path):
        import mysql.connector
        connection = mysql.connector.connect(
            host='gym-database.caxii84umkba.us-east-1.rds.amazonaws.com',
            user='gym_user',
            password='Yulia2006.',
            database='gym_2'
        )
        cursor = connection.cursor()
        with open(sql_file_path, 'r') as sql_file:
            sql_text = sql_file.read()
            sql_statements = sql_text.split(';')
            for statement in sql_statements:
                statement = statement.strip()
                if statement:
                    try:
                        cursor.execute(statement)
                        connection.commit()
                    except mysql.connector.Error as error:
                        print(f"Error executing SQL statement: {error}")
                        connection.rollback()
        cursor.close()
        connection.close()
