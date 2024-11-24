from __future__ import annotations
from app import db


class ProgramDay(db.Model):
    __tablename__ = 'program_days'

    id = db.Column('program_day_id', db.Integer, primary_key=True)
    day = db.Column(db.String(45), nullable=False)

    program = db.relationship(
        'Program',
        back_populates='day',
        uselist=False
    )

    @staticmethod
    def create_from_dto(dto):
        return ProgramDay(
            day=dto['day']
        )

    def put_into_dto(self):
        return {
            'program_day_id': self.id,
            'day': self.day
        }

def insert_program_day(day: str) -> ProgramDay:
    new_program_day = ProgramDay(day=day)
    db.session.add(new_program_day)
    db.session.commit()
    return new_program_day
