from .general_service import GeneralService
from ..dao import program_days_dao

class ProgramDayService(GeneralService):
    _dao = program_days_dao
