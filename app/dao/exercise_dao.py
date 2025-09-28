from app.domain import Exercise
from app.dao.general_dao import GeneralDAO

class ExerciseDAO(GeneralDAO):
    _domain_type = Exercise
