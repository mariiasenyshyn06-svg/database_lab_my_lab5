from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import exercise_criteria_controller
from ..domain.exercise_criteria import ExerciseCriteria

exercise_criteria_bp = Blueprint('exercise-criteria', __name__, url_prefix='/exercise-criteria')

@exercise_criteria_bp.route('', methods=['GET'])
def get_all_exercise_criteria():
    return make_response(jsonify(exercise_criteria_controller.find_all()), HTTPStatus.OK)

@exercise_criteria_bp.route('', methods=['POST'])
def create_exercise_criteria() -> Response:
    content = request.get_json()
    exercise_criteria = ExerciseCriteria.create_from_dto(content)
    exercise_criteria_controller.create(exercise_criteria)
    return make_response(jsonify(exercise_criteria.put_into_dto()), HTTPStatus.CREATED)

@exercise_criteria_bp.route('/<int:criteria_id>', methods=['GET'])
def get_exercise_criteria(criteria_id: int) -> Response:
    exercise_criteria = exercise_criteria_controller.find_by_id(criteria_id)
    if exercise_criteria is None:
        return make_response({"message": "Exercise Criteria not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(exercise_criteria), HTTPStatus.OK)

@exercise_criteria_bp.route('/<int:criteria_id>', methods=['PUT'])
def update_exercise_criteria(criteria_id: int) -> Response:
    content = request.get_json()
    exercise_criteria = ExerciseCriteria.create_from_dto(content)
    exercise_criteria_controller.update(criteria_id, exercise_criteria)
    return make_response("Exercise Criteria updated", HTTPStatus.OK)

@exercise_criteria_bp.route('/<int:criteria_id>', methods=['PATCH'])
def patch_exercise_criteria(criteria_id: int) -> Response:
    content = request.get_json()
    exercise_criteria_controller.patch(criteria_id, content)
    return make_response("Exercise Criteria updated", HTTPStatus.OK)

@exercise_criteria_bp.route('/<int:criteria_id>', methods=['DELETE'])
def delete_exercise_criteria(criteria_id: int) -> Response:
    exercise_criteria_controller.delete(criteria_id)
    return make_response("Exercise Criteria deleted", HTTPStatus.OK)
