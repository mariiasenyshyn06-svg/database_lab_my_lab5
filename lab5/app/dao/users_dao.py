from app.domain import User
from app.dao.general_dao import GeneralDAO

class UserDAO(GeneralDAO):
    _domain_type = User
