from app.domain import ProgramAssignment
from app.dao.general_dao import GeneralDAO

class ProgramAssignmentDAO(GeneralDAO):
    _domain_type = ProgramAssignment
