import mysql.connector
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .config import Config
from .root import register_routes
import os
import sys
from .root.docs_route import docs_bp
from .root.swagger_route import swagger_bp, swagger_ui_bp

print(sys.path)
db = SQLAlchemy()

def register_routes(app):
    app.register_blueprint(docs_bp, url_prefix="")
    app.register_blueprint(swagger_bp, url_prefix="")
    app.register_blueprint(swagger_ui_bp, url_prefix="/swagger")

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    register_routes(app)
    create_database()
    create_tables(app)
    populate_data()
    return app

def create_database():
    try:
        connection = mysql.connector.connect(
            host='gym-database.caxii84umkba.us-east-1.rds.amazonaws.com',  # RDS хост
            user='gym_user',
            password='Yulia2006.',
            database='gym_2'
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS gym_2")
        print("Database created successfully or already exists.")
        cursor.close()
    except mysql.connector.Error as error:
        print(f"Error creating database: {error}")
    finally:
        if 'connection' in locals() and connection.is_connected():
            connection.close()




def create_tables(app):
    with app.app_context():
        db.create_all()


def populate_data():
    sql_file_path = os.path.abspath('data.sql')
    if os.path.exists(sql_file_path):
        connection = mysql.connector.connect(
            host='gym-database.caxii84umkba.us-east-1.rds.amazonaws.com',  # RDS хост
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

