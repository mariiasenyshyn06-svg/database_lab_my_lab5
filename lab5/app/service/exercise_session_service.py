from .general_service import GeneralService
from ..dao import exercise_session_dao

class ExerciseSessionService(GeneralService):
    _dao = exercise_session_dao
