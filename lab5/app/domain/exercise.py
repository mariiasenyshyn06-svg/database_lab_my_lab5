from __future__ import annotations
from app import db
from sqlalchemy import text


class Exercise(db.Model):
    __tablename__ = 'exercise'

    id = db.Column('exercise_id', db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(45))

    program_has_exercises = db.relationship(
        'ProgramsHasExercise',
        back_populates='exercise',
        lazy='dynamic'
    )

    criteria = db.relationship(
        'ExerciseCriteria',
        back_populates='exercise',
        lazy='dynamic'
    )

    exercise_sessions = db.relationship(
        'ExerciseSession',
        back_populates='exercise',
        lazy='dynamic'
    )

    @staticmethod
    def create_from_dto(dto):
        return Exercise(
            name=dto['name'],
            description=dto.get('description')
        )

    def put_into_dto(self):
        return {
            'exercise_id': self.id,
            'name': self.name,
            'description': self.description,
            'criteria': [criterion.put_into_dto() for criterion in self.criteria], # Виведення критеріїв
            'sessions': [session.put_into_dto() for session in self.sessions]
        }

