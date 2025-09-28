from http import HTTPStatus
from flask import Blueprint, jsonify, Response, request, make_response
from ..controller import trainers_has_users_controller
from ..domain.trainers_has_users import TrainersHasUsers
from ..domain.trainers import Trainer
from ..domain.users import User
from datetime import datetime
from app import db

trainers_has_users_bp = Blueprint('trainers-has-users', __name__, url_prefix='/trainers-has-users')


@trainers_has_users_bp.route('', methods=['GET'])
def get_all_trainers():
    try:
        result = TrainersHasUsers.query.all()
        result_dto = [item.put_into_dto() for item in result]

        return make_response(jsonify(result_dto), HTTPStatus.OK)

    except Exception as e:
        return jsonify({'message': str(e)}), 400

@trainers_has_users_bp.route('', methods=['POST'])
def create_trainers_has_users() -> Response:
    content = request.get_json()
    trainers_has_users = TrainersHasUsers.create_from_dto(content)
    trainers_has_users_controller.create(trainers_has_users)
    return make_response(jsonify(trainers_has_users.put_into_dto()), HTTPStatus.CREATED)

@trainers_has_users_bp.route('/<int:trainer_id>/<int:user_id>', methods=['GET'])
def get_trainers_has_users(trainer_id: int, user_id: int) -> Response:
    print(f"Looking for trainers_has_users with trainer_id = {trainer_id} and user_id = {user_id}")
    trainers_has_users = trainers_has_users_controller.find_by_ids(trainer_id, user_id)
    if trainers_has_users is None:
        print(f"TrainersHasUsers not found for trainer_id = {trainer_id} and user_id = {user_id}")
        return make_response({"message": "Trainers Has Users not found"}, HTTPStatus.NOT_FOUND)
    return make_response(jsonify(trainers_has_users.put_into_dto()), HTTPStatus.OK)

@trainers_has_users_bp.route('/<int:trainer_id>/<int:user_id>', methods=['DELETE'])
def delete_trainers_has_users(trainer_id: int, user_id: int) -> Response:
    trainers_has_users_controller.delete(trainer_id, user_id)
    return make_response("Trainers Has Users deleted", HTTPStatus.OK)

@trainers_has_users_bp.route('/<int:trainer_id>/<int:user_id>', methods=['PUT'])
def update_trainers_has_users(trainer_id: int, user_id: int) -> Response:
    content = request.get_json()
    trainers_has_users = TrainersHasUsers.create_from_dto(content)
    trainers_has_users_controller.update(trainer_id, user_id, trainers_has_users)
    return make_response("Trainers Has Users updated", HTTPStatus.OK)

@trainers_has_users_bp.route('/<int:trainer_id>/<int:user_id>', methods=['PATCH'])
def patch_trainers_has_users(trainer_id: int, user_id: int) -> Response:
    content = request.get_json()
    trainers_has_users_controller.patch(trainer_id, user_id, content)
    return make_response("Trainers Has Users updated", HTTPStatus.OK)



@trainers_has_users_bp.route('/add-trainer-user', methods=['POST'])
def add_trainer_user_record():
    try:
        data = request.json
        trainer_name = data['trainer_name']
        user_email = data['user_email']
        start_date = data['start_date']
        end_date = data.get('end_date')

        trainer = Trainer.query.filter_by(first_name=trainer_name).first()
        if not trainer:
            return jsonify({'error': f'Trainer with name {trainer_name} not found'}), 400

        user = User.query.filter_by(email=user_email).first()
        if not user:
            return jsonify({'error': f'User with email {user_email} not found'}), 400

        new_record = TrainersHasUsers(
            trainer_id=trainer.id,
            user_id=user.id,
            start_date=start_date,
            end_date=end_date
        )

        db.session.add(new_record)
        db.session.commit()
        return jsonify({'message': 'Trainer-User relation added successfully'}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400
