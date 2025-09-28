from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import users_controller
from ..domain.users import User

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('', methods=['GET'])
def get_all_users():
    return make_response(jsonify(users_controller.find_all()), HTTPStatus.OK)

@user_bp.route('', methods=['POST'])
def create_user() -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    users_controller.create(user)
    return make_response(jsonify(user.put_into_dto()), HTTPStatus.CREATED)

@user_bp.route('/<int:users_id>', methods=['GET'])
def get_user(users_id: int) -> Response:
    user = users_controller.find_by_id(users_id)
    if user is None:
        return make_response({"message": "User not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(user), HTTPStatus.OK)

@user_bp.route('/<int:users_id>', methods=['PUT'])
def update_user(users_id: int) -> Response:
    content = request.get_json()
    user = User.create_from_dto(content)
    users_controller.update(users_id, user)
    return make_response("User updated", HTTPStatus.OK)

@user_bp.route('/<int:users_id>', methods=['PATCH'])
def patch_user(users_id: int) -> Response:
    content = request.get_json()
    users_controller.patch(users_id, content)
    return make_response("User updated", HTTPStatus.OK)

@user_bp.route('/<int:users_id>', methods=['DELETE'])
def delete_user(users_id: int) -> Response:
    users_controller.delete(users_id)
    return make_response("User deleted", HTTPStatus.OK)
