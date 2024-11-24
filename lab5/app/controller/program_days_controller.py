from .general_controller import GeneralController
from ..service import program_days_service
from flask_restful import Resource

class ProgramDayController(GeneralController, Resource):
    _service = program_days_service
