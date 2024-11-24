from .general_controller import GeneralController
from ..service import exercise_session_service
from flask_restful import Resource

class ExerciseSessionController(GeneralController, Resource):
    _service = exercise_session_service
