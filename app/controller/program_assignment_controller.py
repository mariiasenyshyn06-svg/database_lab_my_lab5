from .general_controller import GeneralController
from ..service import program_assignment_service
from flask_restful import Resource

class ProgramAssignmentController(GeneralController, Resource):
    _service = program_assignment_service
