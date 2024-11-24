from __future__ import annotations
from app import db
from sqlalchemy import func


class ExerciseSession(db.Model):
    __tablename__ = 'exercise_session'

    id = db.Column('session_id', db.Integer, primary_key=True)
    assignment_id = db.Column(db.Integer, db.ForeignKey('program_assignment.assignment_id'))
    exercise_id = db.Column(db.Integer, db.ForeignKey('exercise.exercise_id'))
    session_date = db.Column(db.Date, nullable=False)

    assignment = db.relationship('ProgramAssignment')
    exercise = db.relationship('Exercise', back_populates='exercise_sessions')

    @staticmethod
    def create_from_dto(dto):
        return ExerciseSession(
            assignment_id=dto['assignment_id'],
            exercise_id=dto['exercise_id'],
            session_date=dto['session_date']
        )

    def put_into_dto(self):
        return {
            'session_id': self.id,
            'assignment_id': self.assignment_id,
            'exercise_id': self.exercise_id,
            'session_date': self.session_date.isoformat()
        }

def get_exercise_sessions_stat(stat_type: str, exercise_id: int):
    """
    Отримує статистику по сесіям вправ за типом stat_type.

    :param stat_type: Тип статистики ('MAX', 'MIN', 'SUM', 'AVG').
    :param exercise_id: ID вправи для фільтрації сесій.
    :return: Статистика за запитом або -1 для помилки.
    """
    if stat_type == 'MAX':
        result = db.session.query(func.max(ExerciseSession.id)).filter(ExerciseSession.exercise_id == exercise_id).scalar()
        return result
    elif stat_type == 'MIN':
        result = db.session.query(func.min(ExerciseSession.id)).filter(ExerciseSession.exercise_id == exercise_id).scalar()
        return result
    elif stat_type == 'SUM':
        result = db.session.query(func.count(ExerciseSession.id)).filter(ExerciseSession.exercise_id == exercise_id).scalar()
        return result
    elif stat_type == 'AVG':
        result = db.session.query(func.avg(ExerciseSession.id)).filter(ExerciseSession.exercise_id == exercise_id).scalar()
        return result
    else:
        return -1
