from .general_controller import GeneralController
from app.service import users_service
from flask_restful import Resource


class UserController(GeneralController, Resource):
    _service = users_service