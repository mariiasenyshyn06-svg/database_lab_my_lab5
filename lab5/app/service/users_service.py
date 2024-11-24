from .general_service import GeneralService
from ..dao import users_dao

class UserService(GeneralService):
    _dao = users_dao
