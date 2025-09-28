from app.domain import Trainer
from app.dao.general_dao import GeneralDAO

class TrainerDAO(GeneralDAO):
    _domain_type = Trainer
