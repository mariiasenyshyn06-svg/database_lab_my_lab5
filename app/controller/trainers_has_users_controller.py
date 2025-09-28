from ..controller.general_controller import GeneralController  #
from ..service.trainers_has_users_service import TrainerHasUserService
from ..domain.trainers_has_users import TrainersHasUsers
from flask_restful import Resource
from app import db
from app.service.trainers_has_users_service import trainers_has_users_service

class TrainerHasUserController(GeneralController, Resource):
    _service = TrainerHasUserService

    @staticmethod
    def find_by_ids(trainer_id: int, user_id: int) -> TrainersHasUsers:
        return TrainersHasUsers.query.filter_by(trainer_id=trainer_id, user_id=user_id).first()

    def find_all(self):
        return trainers_has_users_service.find_all()

    @staticmethod
    def find_by_relation_id(relation_id: int) -> TrainersHasUsers:
        return TrainersHasUsers.query.get(relation_id)

    def delete(self, trainer_id: int, user_id: int) -> None:
        trainers_has_users = self.find_by_ids(trainer_id, user_id)
        if trainers_has_users:
            db.session.delete(trainers_has_users)
            db.session.commit()
