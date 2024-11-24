from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response, current_app
from ..controller import exercise_controller
from ..domain.exercise import Exercise



exercise_bp = Blueprint('exercise', __name__, url_prefix='/exercise')

@exercise_bp.route('', methods=['GET'])
def get_all_exercises():
    return make_response(jsonify(exercise_controller.find_all()), HTTPStatus.OK)

@exercise_bp.route('', methods=['POST'])
def create_exercise() -> Response:
    content = request.get_json()
    exercise = Exercise.create_from_dto(content)
    exercise_controller.create(exercise)
    return make_response(jsonify(exercise.put_into_dto()), HTTPStatus.CREATED)


@exercise_bp.route('/<int:exercise_id>', methods=['GET'])
def get_exercise(exercise_id: int) -> Response:
    exercise = exercise_controller.find_by_id(exercise_id)
    if exercise is None:
        return make_response({"message": "Exercise not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(exercise), HTTPStatus.OK)

@exercise_bp.route('/<int:exercise_id>', methods=['PUT'])
def update_exercise(exercise_id: int) -> Response:
    content = request.get_json()
    exercise = Exercise.create_from_dto(content)
    exercise_controller.update(exercise_id, exercise)
    return make_response("Exercise updated", HTTPStatus.OK)

@exercise_bp.route('/<int:exercise_id>', methods=['PATCH'])
def patch_exercise(exercise_id: int) -> Response:
    content = request.get_json()
    exercise_controller.patch(exercise_id, content)
    return make_response("Exercise updated", HTTPStatus.OK)

@exercise_bp.route('/<int:exercise_id>', methods=['DELETE'])
def delete_exercise(exercise_id: int) -> Response:
    exercise_controller.delete(exercise_id)
    return make_response("Exercise deleted", HTTPStatus.OK)

@exercise_bp.route('/<int:exercise_id>/criteria', methods=['GET'])
def get_criteria_for_exercise(exercise_id: int):
    try:
        exercise = Exercise.query.get(exercise_id)
        if not exercise:
            return make_response({"message": "Exercise not found"}, HTTPStatus.NOT_FOUND)

        criteria = exercise.criteria.all()
        if not criteria:
            return make_response({"message": "No criteria found for this exercise"}, HTTPStatus.NOT_FOUND)

        result_dto = [item.put_into_dto() for item in criteria]

        result_dto_with_name = {
            "exercise_name": exercise.name,
            "criteria": result_dto
        }
        return make_response(jsonify(result_dto_with_name), HTTPStatus.OK)
    except Exception as e:
        return make_response({"message": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)

@exercise_bp.route('/<int:exercise_id>/sessions', methods=['GET'])
def get_sessions_for_exercise(exercise_id: int):
    try:
        exercise = Exercise.query.get(exercise_id)
        if not exercise:
            return make_response({"message": "Exercise not found"}, HTTPStatus.NOT_FOUND)
        sessions = exercise.exercise_sessions.all()

        if not sessions:
            return make_response({"message": "No sessions found for this exercise"}, HTTPStatus.NOT_FOUND)

        result_dto = [session.put_into_dto() for session in sessions]

        result_dto_with_name = {
            "exercise_name": exercise.name,
            "sessions": result_dto
        }
        return make_response(jsonify(result_dto_with_name), HTTPStatus.OK)
    except Exception as e:
        return make_response({"message": str(e)}, HTTPStatus.INTERNAL_SERVER_ERROR)


