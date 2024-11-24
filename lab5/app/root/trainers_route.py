from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import trainers_controller
from ..domain.trainers import Trainer
from ..domain.trainers import insert_trainers_data

trainer_bp = Blueprint('trainer', __name__, url_prefix='/trainer')

@trainer_bp.route('', methods=['GET'])
def get_all_trainers():
    return make_response(jsonify(trainers_controller.find_all()), HTTPStatus.OK)

@trainer_bp.route('', methods=['POST'])
def create_trainer() -> Response:
    content = request.get_json()
    trainer = Trainer.create_from_dto(content)
    trainers_controller.create(trainer)
    return make_response(jsonify(trainer.put_into_dto()), HTTPStatus.CREATED)

@trainer_bp.route('/<int:trainer_id>', methods=['GET'])
def get_trainer(trainer_id: int) -> Response:
    trainer = trainers_controller.find_by_id(trainer_id)
    if trainer is None:
        return make_response({"message": "Trainer not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(trainer), HTTPStatus.OK)

@trainer_bp.route('/<int:trainer_id>', methods=['PUT'])
def update_trainer(trainer_id: int) -> Response:
    content = request.get_json()
    trainer = Trainer.create_from_dto(content)
    trainers_controller.update(trainer_id, trainer)
    return make_response("Trainer updated", HTTPStatus.OK)

@trainer_bp.route('/<int:trainer_id>', methods=['PATCH'])
def patch_trainer(trainer_id: int) -> Response:
    content = request.get_json()
    trainers_controller.patch(trainer_id, content)
    return make_response("Trainer updated", HTTPStatus.OK)

@trainer_bp.route('/<int:trainer_id>', methods=['DELETE'])
def delete_trainer(trainer_id: int) -> Response:
    trainers_controller.delete(trainer_id)
    return make_response("Trainer deleted", HTTPStatus.OK)

@trainer_bp.route('/add-trainers-data', methods=['POST'])
def add_trainers_data() -> Response:
    result = insert_trainers_data()
    if "Помилка" in result:
        return make_response({"message": result}, HTTPStatus.INTERNAL_SERVER_ERROR)
    return make_response({"message": result}, HTTPStatus.CREATED)

