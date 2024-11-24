from .general_service import GeneralService
from ..dao import exercise_dao

class ExerciseService(GeneralService):
    _dao = exercise_dao
