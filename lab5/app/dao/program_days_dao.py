from app.domain import ProgramDay
from app.dao.general_dao import GeneralDAO

class ProgramDayDAO(GeneralDAO):
    _domain_type = ProgramDay
