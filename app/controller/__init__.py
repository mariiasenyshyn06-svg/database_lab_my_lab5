# app/controllers/__init__.py

from .users_controller import UserController
from .trainers_controller import TrainerController
from .programs_controller import ProgramController
from .exercise_controller import ExerciseController
from .program_assignment_controller import ProgramAssignmentController
from .programs_has_exercise_controller import ProgramsHasExerciseController
from .exercise_session_controller import ExerciseSessionController
from .program_days_controller import ProgramDayController
from .exercise_criteria_controller import ExerciseCriteriaController
from .trainers_has_users_controller import TrainerHasUserController
from .users_controller import UserController
from .user_feedback_controller import UserFeedbackController

users_controller = UserController()
trainers_controller = TrainerController()
programs_controller = ProgramController()
exercise_controller = ExerciseController()
program_assignment_controller = ProgramAssignmentController()
programs_has_exercise_controller = ProgramsHasExerciseController()
exercise_session_controller = ExerciseSessionController()
program_days_controller = ProgramDayController()
exercise_criteria_controller = ExerciseCriteriaController()
trainers_has_users_controller = TrainerHasUserController()
user_feedback_controller = UserFeedbackController()