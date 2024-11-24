from app.domain import TrainersHasUsers
from app.dao.general_dao import GeneralDAO

class TrainerHasUserDAO(GeneralDAO):
    _domain_type = TrainersHasUsers

    def add_trainer_user(trainer_name: str, user_email: str, start_date: str, end_date: str | None = None):
        return TrainersHasUsers.insert_record(trainer_name, user_email, start_date, end_date)
