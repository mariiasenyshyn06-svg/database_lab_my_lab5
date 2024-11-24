from __future__ import annotations
from app import db
from app.domain.users import User
from app.domain.trainers import Trainer


class TrainersHasUsers(db.Model):
    __tablename__ = 'trainers_has_users'

    trainer_id = db.Column(db.Integer, db.ForeignKey('trainers.trainer_id'), primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.users_id'), primary_key=True)

    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

    trainer = db.relationship('Trainer', backref=db.backref('trainer_users', lazy=True))

    user = db.relationship('User', backref=db.backref('user_trainers', lazy=True), overlaps="trainers,users")

    @staticmethod
    def create_from_dto(dto):
        return TrainersHasUsers(
            trainer_id=dto['trainer_id'],
            user_id=dto['user_id'],
            start_date=dto['start_date'],
            end_date=dto.get('end_date')
        )

    def put_into_dto(self):
        return {
            'trainer_id': self.trainer_id,
            'user_id': self.user_id,
            'trainer_name': f'{self.trainer.first_name} {self.trainer.last_name}',
            'user_name': f'{self.user.first_name} {self.user.last_name}',
            'start_date': self.start_date,
            'end_date': self.end_date
        }

    @staticmethod
    def insert_record(trainer_name: str, user_email: str, start_date: str, end_date: str | None = None):
        try:
            trainer = Trainer.query.filter_by(first_name=trainer_name).first()
            if not trainer:
                raise ValueError(f"Trainer with name '{trainer_name}' not found.")

            user = User.query.filter_by(email=user_email).first()
            if not user:
                raise ValueError(f"User with email '{user_email}' not found.")

            record = TrainersHasUsers(
                trainer_id=trainer.id,
                user_id=user.id,
                start_date=start_date,
                end_date=end_date
            )
            db.session.add(record)
            db.session.commit()
            return record.put_into_dto()
        except Exception as e:
            db.session.rollback()
            raise ValueError(f"Error inserting record: {e}")