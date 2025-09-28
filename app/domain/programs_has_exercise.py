from __future__ import annotations
from app import db



class ProgramsHasExercise(db.Model):
    __tablename__ = 'programs_has_exercise'

    program_id = db.Column(db.Integer, db.ForeignKey('programs.program_id'), primary_key=True)
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.exercise_id'), primary_key=True)
    program_exercise_id = db.Column(db.Integer, primary_key=True)

    duration = db.Column(db.Integer)
    repetition = db.Column(db.Integer)
    criteria = db.Column(db.String(100))

    program = db.relationship('Program', back_populates='exercises')
    exercise = db.relationship('Exercise', back_populates='program_has_exercises')

    def put_into_dto(self):
        return {
            'program_name': self.program.name,
            'exercise_name': self.exercise.name,
            'duration': self.duration,
            'repetition': self.repetition,
            'criteria': self.criteria
        }