from .general_service import GeneralService
from ..dao import programs_dao

class ProgramService(GeneralService):
    _dao = programs_dao
