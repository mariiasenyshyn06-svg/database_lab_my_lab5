from .general_controller import GeneralController
from ..service import programs_service
from flask_restful import Resource

class ProgramController(GeneralController, Resource):
    _service = programs_service