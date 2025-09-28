# app/routes.py

from flask import Flask
from app.root.error_handler import err_handler_bp

def register_routes(app: Flask) -> None:
    # Реєструємо обробники помилок
    app.register_blueprint(err_handler_bp)

    # Імпортуємо маршрутизатори для кожної таблиці вашої бази даних gym_manager
    from .users_route import user_bp
    from .trainers_route import trainer_bp
    from .programs_route import program_bp
    from .exercise_route import exercise_bp
    from .program_assignment_route import program_assignment_bp
    from .programs_has_exercise_route import programs_has_exercise_bp
    from .exercise_session_route import exersice_session_bp
    from .program_days_route import program_days_bp
    from .exercise_criteria_route import exercise_criteria_bp
    from .trainers_has_users_route import trainers_has_users_bp
    from .user_feedback_route import user_feedback_bp

    # Реєструємо маршрутизатори
    app.register_blueprint(user_bp)
    app.register_blueprint(trainer_bp)
    app.register_blueprint(program_bp)
    app.register_blueprint(exercise_bp)
    app.register_blueprint(program_assignment_bp)
    app.register_blueprint(programs_has_exercise_bp)
    app.register_blueprint(exersice_session_bp)
    app.register_blueprint(program_days_bp)
    app.register_blueprint(exercise_criteria_bp)
    app.register_blueprint(trainers_has_users_bp)
    app.register_blueprint(user_feedback_bp)
