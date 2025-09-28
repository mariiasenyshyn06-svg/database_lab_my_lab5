from __future__ import annotations
from typing import Dict, Any
from app import db


class ProgramAssignment(db.Model):
    __tablename__ = 'program_assignment'

    id = db.Column('assignment_id', db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.users_id'), nullable=False)
    program_id = db.Column(db.Integer, db.ForeignKey('programs.program_id'), nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.trainer_id'), nullable=False)
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)


    user = db.relationship('User', backref=db.backref('program_assignments', lazy=True))
    program = db.relationship('Program', backref=db.backref('assignments', lazy=True))
    trainer = db.relationship('Trainer', backref=db.backref('assignments', lazy=True))

    @staticmethod
    def create_from_dto(dto):
        return ProgramAssignment(
            user_id=dto['user_id'],
            program_id=dto['program_id'],
            trainer_id=dto['trainer_id'],
            start_date=dto['start_date'],
            end_date=dto['end_date']
        )

    def put_into_dto(self):
        return {
            'assignment_id': self.id,
            'user_id': self.user_id,
            'program_id': self.program_id,
            'trainer_id': self.trainer_id,
            'start_date': self.start_date,
            'end_date': self.end_date
        }