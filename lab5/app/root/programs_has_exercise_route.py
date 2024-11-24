from flask import Blueprint, request, jsonify, make_response, current_app
from app import db
from app.domain import ProgramsHasExercise
from http import HTTPStatus

programs_has_exercise_bp = Blueprint('programs_has_exercise', __name__, url_prefix='/programs_has_exercise')


@programs_has_exercise_bp.route('/programs_has_exercise', methods=['POST'])
def create_program_has_exercise():
    try:
        data = request.get_json()
        new_program_has_exercise = ProgramsHasExercise(
            program_id=data['program_id'],
            exercise_id=data['exercise_id'],
            program_exercise_id=data['program_exercise_id'],
            duration=data.get('duration'),
            repetition=data.get('repetition'),
            criteria=data.get('criteria')
        )

        db.session.add(new_program_has_exercise)
        db.session.commit()

        return jsonify({'message': 'Created successfully', 'id': new_program_has_exercise.program_exercise_id}), 201

    except Exception as e:
        return jsonify({'message': str(e)}), 400


@programs_has_exercise_bp.route('/programs_has_exercise', methods=['GET'])
def get_all_programs_has_exercise():
    try:
        result = ProgramsHasExercise.query.all()

        if not result:
            current_app.logger.warning("No records found in programs_has_exercise")

        result_dto = [item.put_into_dto() for item in result]
        return make_response(jsonify(result_dto), HTTPStatus.OK)

    except Exception as e:
        current_app.logger.error(f"Error: {str(e)}")
        return jsonify({'message': str(e)}), 400

@programs_has_exercise_bp.route('/<int:program_id>/<int:exercise_id>', methods=['GET'])
def get_programs_has_exercise(program_id: int, exercise_id: int):
    program_has_exercise = ProgramsHasExercise.query.filter_by(
        program_id=program_id,
        exercise_id=exercise_id,
    ).first()

    if program_has_exercise is None:
        return make_response({"message": "Programs Has Exercise not found"}, HTTPStatus.NOT_FOUND)

    return make_response(jsonify(program_has_exercise.put_into_dto()), HTTPStatus.OK)


@programs_has_exercise_bp.route('/programs_has_exercise/<int:id>', methods=['PUT'])
def update_program_has_exercise(id):
    try:
        program_has_exercise = ProgramsHasExercise.query.get_or_404(id)

        data = request.get_json()
        program_has_exercise.program_id = data['program_id']
        program_has_exercise.exercise_id = data['exercise_id']
        program_has_exercise.duration = data.get('duration', program_has_exercise.duration)
        program_has_exercise.repetition = data.get('repetition', program_has_exercise.repetition)
        program_has_exercise.criteria = data.get('criteria', program_has_exercise.criteria)

        db.session.commit()

        return jsonify({'message': 'Updated successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400

@programs_has_exercise_bp.route('/programs_has_exercise/<int:id>', methods=['DELETE'])
def delete_program_has_exercise(id):
    try:
        program_has_exercise = ProgramsHasExercise.query.get_or_404(id)

        db.session.delete(program_has_exercise)
        db.session.commit()

        return jsonify({'message': 'Deleted successfully'}), 200
    except Exception as e:
        return jsonify({'message': str(e)}), 400


@programs_has_exercise_bp.route('/exercise/<int:exercise_id>', methods=['GET'])
def get_programs_by_exercise(exercise_id: int):
    try:
        result = ProgramsHasExercise.query.filter_by(exercise_id=exercise_id).all()

        if not result:
            return make_response({"message": "No programs found for this exercise"}, HTTPStatus.NOT_FOUND)

        result_dto = [item.put_into_dto() for item in result]

        return make_response(jsonify(result_dto), HTTPStatus.OK)
    except Exception as e:
        current_app.logger.error(f"Error: {str(e)}")
        return jsonify({'message': str(e)}), 400

@programs_has_exercise_bp.route('/program/<int:program_id>', methods=['GET'])
def get_exercises_by_program(program_id: int):
    try:
        result = ProgramsHasExercise.query.filter_by(program_id=program_id).all()

        if not result:
            return make_response({"message": "No exercises found for this program"}, HTTPStatus.NOT_FOUND)

        result_dto = [item.put_into_dto() for item in result]

        return make_response(jsonify(result_dto), HTTPStatus.OK)
    except Exception as e:
        current_app.logger.error(f"Error: {str(e)}")
        return jsonify({'message': str(e)}), 400
