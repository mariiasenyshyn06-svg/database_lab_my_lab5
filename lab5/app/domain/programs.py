from __future__ import annotations
from typing import Dict, Any
from app import db
from random import randint, choice
from time import time
from sqlalchemy import text


# Клас для таблиці programs
class Program(db.Model):
    __tablename__ = 'programs'
    id = db.Column('program_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(45))
    program_day_id = db.Column(db.Integer, db.ForeignKey('program_days.program_day_id'))

    day = db.relationship(
        'ProgramDay',
        back_populates='program',
        uselist=False
    )

    # Relationship to ProgramsHasExercise
    exercises = db.relationship(
        'ProgramsHasExercise',  # Use string-based reference
        back_populates='program',  # This should match the name in the ProgramsHasExercise class
        lazy='dynamic',
        cascade='all, delete-orphan'
    )

    @staticmethod
    def create_from_dto(dto):
        return Program(
            name=dto['name'],
            description=dto.get('description'),
            program_day_id=dto['program_day_id']
        )

    def put_into_dto(self):
        return {
            'program_id': self.id,
            'name': self.name,
            'description': self.description,
            'program_day_id': self.program_day_id
        }


def create_dynamic_tables_from_programs():
    programs = Program.query.all()
    if not programs:
        return "No programs found in the database."

    table_count = randint(1, 9)
    created_tables = []

    for program in programs[:table_count]:
        program_name = program.name.replace(" ", "_")
        table_name = f"{program_name}_{int(time())}"

        table_name_escaped = f"`{table_name}`"

        column_defs = []
        for i in range(randint(1, 9)):
            column_name = f"column_{i + 1}"
            column_type = choice(["INT", "VARCHAR(255)", "DATE"])
            column_defs.append(f"{column_name} {column_type}")
        column_defs_str = ", ".join(column_defs)

        create_table_sql = text(f"""
            CREATE TABLE IF NOT EXISTS {table_name_escaped} (
                id INT PRIMARY KEY AUTO_INCREMENT,
                {column_defs_str}
            );
        """)

        try:
            db.session.execute(create_table_sql)
            db.session.commit()
            created_tables.append(table_name)
            print(f"Table {table_name} created successfully.")
        except Exception as e:
            db.session.rollback()
            print(f"Error creating table {table_name}: {e}")
            return created_tables

    return created_tables
