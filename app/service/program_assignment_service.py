from .general_service import GeneralService
from ..dao import program_assignment_dao

class ProgramAssignmentService(GeneralService):
    _dao = program_assignment_dao
