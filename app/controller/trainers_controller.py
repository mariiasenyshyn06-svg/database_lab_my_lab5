from .general_controller import GeneralController
from ..service import trainers_service
from flask_restful import Resource

class TrainerController(GeneralController, Resource):
    _service = trainers_service