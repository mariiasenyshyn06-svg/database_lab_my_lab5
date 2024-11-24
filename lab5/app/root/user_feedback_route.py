from http import HTTPStatus
from flask import Blueprint, jsonify, request, make_response
from ..controller.user_feedback_controller import UserFeedbackController
from app import db
from ..domain.user_feedback import UserFeedback
from ..domain.users import User

user_feedback_bp = Blueprint('user_feedback', __name__, url_prefix='/user_feedback')
user_feedback_controller = UserFeedbackController()

@user_feedback_bp.route('', methods=['POST'])
def add_feedback():
    content = request.get_json()

    try:
        new_feedback = UserFeedback.create_from_dto(content)

        db.session.add(new_feedback)
        db.session.commit()

        return make_response(jsonify(new_feedback.put_into_dto()), HTTPStatus.CREATED)

    except ValueError as e:
        return make_response(jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST)

    except Exception as e:
        return make_response(jsonify({'error': 'An error occurred', 'details': str(e)}), HTTPStatus.INTERNAL_SERVER_ERROR)

@user_feedback_bp.route('/<int:feedback_id>', methods=['GET'])
def get_feedback(feedback_id: int):
    feedback = user_feedback_controller.find_by_id(feedback_id)
    if feedback is None:
        return make_response({"message": "Feedback not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(feedback), HTTPStatus.OK)

@user_feedback_bp.route('/user/<int:user_id>', methods=['GET'])
def get_feedbacks_by_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return make_response({"message": "User not found"}, HTTPStatus.NOT_FOUND)

    feedbacks = UserFeedback.query.filter_by(user_id=user_id).all()
    result = [
        {"trainer_id": f.trainer_id, "feedback_text": f.feedback_text, "rating": f.rating}
        for f in feedbacks
    ]

    return make_response(jsonify(result), HTTPStatus.OK)

@user_feedback_bp.route('/<int:feedback_id>', methods=['PUT'])
def update_feedback(feedback_id: int):
    content = request.get_json()
    user_feedback_controller.update(feedback_id, content)
    return make_response("Feedback updated", HTTPStatus.OK)

@user_feedback_bp.route('/<int:feedback_id>', methods=['PATCH'])
def patch_feedback(feedback_id: int):
    content = request.get_json()
    user_feedback_controller.patch(feedback_id, content)
    return make_response("Feedback updated", HTTPStatus.OK)

@user_feedback_bp.route('/<int:feedback_id>', methods=['DELETE'])
def delete_feedback(feedback_id: int):
    user_feedback_controller.delete(feedback_id)
    return make_response("Feedback deleted", HTTPStatus.OK)

@user_feedback_bp.route('/rating/stat', methods=['GET'])
def get_rating_stat():
    stat_type = request.args.get('stat_type', '').upper()  # Тип статистики (наприклад, MAX)
    if stat_type not in {'MAX', 'MIN', 'SUM', 'AVG'}:
        return make_response(
            jsonify({"error": "Invalid stat_type. Use MAX, MIN, SUM, or AVG"}), HTTPStatus.BAD_REQUEST
        )

    stat_result = UserFeedback.get_rating_stat(stat_type)
    if stat_result is not None:
        return jsonify({stat_type: stat_result})
    else:
        return jsonify({"error": "Statistic calculation failed"}), HTTPStatus.INTERNAL_SERVER_ERROR
