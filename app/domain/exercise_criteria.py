from __future__ import annotations
from app import db


class ExerciseCriteria(db.Model):
    __tablename__ = 'exercise_criteria'

    id = db.Column('criteria_id', db.Integer, primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.exercise_id'))
    criteria_type = db.Column(db.String(50), nullable=False)
    criteria_value = db.Column(db.Integer, nullable=False)

    exercise = db.relationship('Exercise', back_populates='criteria')

    @staticmethod
    def create_from_dto(dto):
        return ExerciseCriteria(
            exercise_id=dto['exercise_id'],
            criteria_type=dto['criteria_type'],
            criteria_value=dto['criteria_value']
        )

    def put_into_dto(self):
        return {
            'criteria_id': self.id,
            'exercise_id': self.exercise_id,
            'criteria_type': self.criteria_type,
            'criteria_value': self.criteria_value
        }
