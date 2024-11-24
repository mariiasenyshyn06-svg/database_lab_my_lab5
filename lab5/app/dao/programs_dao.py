from app.domain import Program
from app.dao.general_dao import GeneralDAO

class ProgramDAO(GeneralDAO):
    _domain_type = Program
