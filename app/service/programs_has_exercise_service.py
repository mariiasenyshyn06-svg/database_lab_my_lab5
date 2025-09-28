from .general_service import GeneralService
from ..dao import programs_has_exercise_dao

class ProgramsHasExerciseService(GeneralService):
    _dao = programs_has_exercise_dao
