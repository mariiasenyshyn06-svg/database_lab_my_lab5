from .general_controller import GeneralController
from ..service import programs_has_exercise_service
from flask_restful import Resource

class ProgramsHasExerciseController(GeneralController, Resource):
    _service = programs_has_exercise_service

