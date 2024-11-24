from .general_service import GeneralService
from ..dao import exercise_criteria_dao

class ExerciseCriteriaService(GeneralService):
    _dao = exercise_criteria_dao
