from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import program_days_controller
from ..domain.program_days import ProgramDay, insert_program_day

program_days_bp = Blueprint('program_days', __name__, url_prefix='/program_days')

@program_days_bp.route('', methods=['GET'])
def get_all_program_days():
    return make_response(jsonify(program_days_controller.find_all()), HTTPStatus.OK)

@program_days_bp.route('', methods=['POST'])
def create_program_day() -> Response:
    content = request.get_json()
    program_day = ProgramDay.create_from_dto(content)
    program_days_controller.create(program_day)
    return make_response(jsonify(program_day.put_into_dto()), HTTPStatus.CREATED)

@program_days_bp.route('/parametrized', methods=['POST'])
def insert_parametrized_program_day() -> Response:
    content = request.get_json()
    new_program_day = insert_program_day(
        day=content['day']
    )
    return make_response(jsonify(new_program_day.put_into_dto()), HTTPStatus.CREATED)

@program_days_bp.route('/<int:day_id>', methods=['GET'])
def get_program_day(day_id: int) -> Response:
    program_day = program_days_controller.find_by_id(day_id)
    if program_day is None:
        return make_response({"message": "Program Day not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(program_day), HTTPStatus.OK)

@program_days_bp.route('/<int:day_id>', methods=['PUT'])
def update_program_day(day_id: int) -> Response:
    content = request.get_json()
    program_day = ProgramDay.create_from_dto(content)
    program_days_controller.update(day_id, program_day)
    return make_response("Program Day updated", HTTPStatus.OK)

@program_days_bp.route('/<int:day_id>', methods=['PATCH'])
def patch_program_day(day_id: int) -> Response:
    content = request.get_json()
    program_days_controller.patch(day_id, content)
    return make_response("Program Day updated", HTTPStatus.OK)

@program_days_bp.route('/<int:day_id>', methods=['DELETE'])
def delete_program_day(day_id: int) -> Response:
    program_days_controller.delete(day_id)
    return make_response("Program Day deleted", HTTPStatus.OK)
