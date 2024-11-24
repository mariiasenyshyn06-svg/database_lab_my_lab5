from __future__ import annotations
from app import db
import random
import string
class Trainer(db.Model):
    __tablename__ = 'trainers'

    id = db.Column('trainer_id', db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    email = db.Column(db.String(100), unique=True)

    users = db.relationship('User', secondary='trainers_has_users', back_populates='trainers', overlaps='trainers')


    @staticmethod
    def create_from_dto(dto):
        return Trainer(
            first_name=dto['first_name'],
            last_name=dto['last_name'],
            email=dto['email']
        )

    def put_into_dto(self):
        return {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email
        }


def generate_random_email(name: str, index: int) -> str:
    domain = "@example.com"
    return f"{name.lower()}{index}{domain}"

def insert_trainers_data():
    try:
        for i in range(1, 11):
            first_name = f"Noname{i}"
            last_name = f"Lastname{i}"
            email = generate_random_email(first_name, i)

            if db.session.query(Trainer).filter_by(email=email).first():
                return f"Тренер з email {email} вже існує."

            new_trainer = Trainer(
                first_name=first_name,
                last_name=last_name,
                email=email
            )

            db.session.add(new_trainer)

        db.session.commit()
        return "10 записів тренерів успішно додано."

    except Exception as e:
        db.session.rollback()
        return f"Помилка при додаванні записів: {e}"
