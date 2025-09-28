from .general_controller import GeneralController
from ..service import exercise_criteria_service
from flask_restful import Resource

class ExerciseCriteriaController(GeneralController, Resource):
    _service = exercise_criteria_service
