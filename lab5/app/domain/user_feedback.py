from __future__ import annotations
from app import db
from datetime import datetime
from sqlalchemy import event, select, func



class UserFeedback(db.Model):
    __tablename__ = 'user_feedback'

    feedback_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, nullable=False)
    trainer_id = db.Column(db.Integer, nullable=False)
    feedback_text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def put_into_dto(self):
        return {
            'feedback_id': self.feedback_id,
            'user_id': self.user_id,
            'trainer_id': self.trainer_id,
            'feedback_text': self.feedback_text,
            'rating': self.rating,
            'created_at': self.created_at
        }

    @staticmethod
    def create_from_dto(dto_dict) -> UserFeedback:
        return UserFeedback(
            user_id=dto_dict.get('user_id'),
            trainer_id=dto_dict.get('trainer_id'),
            feedback_text=dto_dict.get('feedback_text'),
            rating=dto_dict.get('rating'),
            created_at=dto_dict.get('created_at', datetime.utcnow())
        )

    @staticmethod
    def get_rating_stat(stat_type: str):
        if stat_type == 'MAX':
            return db.session.query(func.max(UserFeedback.rating)).scalar()
        elif stat_type == 'MIN':
            return db.session.query(func.min(UserFeedback.rating)).scalar()
        elif stat_type == 'SUM':
            return db.session.query(func.sum(UserFeedback.rating)).scalar()
        elif stat_type == 'AVG':
            return db.session.query(func.avg(UserFeedback.rating)).scalar()
        else:
            return None

@event.listens_for(UserFeedback, "before_insert")
def check_user_exists(mapper, connection, target):
    users_table = db.Table('users', db.metadata, autoload_with=db.engine)

    user_exists = connection.execute(
        select(users_table.c.users_id).where(users_table.c.users_id == target.user_id)
    ).first()

    if not user_exists:
        raise ValueError(f"User with ID {target.user_id} does not exist in the 'users' table.")
