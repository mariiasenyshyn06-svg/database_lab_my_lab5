from app.domain import ExerciseSession
from app.dao.general_dao import GeneralDAO

class ExerciseSessionDAO(GeneralDAO):
    _domain_type = ExerciseSession
