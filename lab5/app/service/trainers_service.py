from .general_service import GeneralService
from ..dao import trainers_dao

class TrainerService(GeneralService):
    _dao = trainers_dao
