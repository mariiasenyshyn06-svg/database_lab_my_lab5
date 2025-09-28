from .general_service import GeneralService
from ..dao import trainers_has_users_dao

class TrainerHasUserService(GeneralService):
    _dao = trainers_has_users_dao

trainers_has_users_service = TrainerHasUserService()
