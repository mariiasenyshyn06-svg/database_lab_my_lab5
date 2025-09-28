from .general_controller import GeneralController
from ..service import exercise_service
from flask_restful import Resource

class ExerciseController(GeneralController, Resource):
    _service = exercise_service
