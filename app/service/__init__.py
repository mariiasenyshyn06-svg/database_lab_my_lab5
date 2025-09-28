# app/services/__init__.py

from .users_service import UserService
from .trainers_service import TrainerService
from .programs_service import ProgramService
from .exercise_service import ExerciseService
from .program_assignment_service import ProgramAssignmentService
from .programs_has_exercise_service import ProgramsHasExerciseService
from .exercise_session_service import ExerciseSessionService
from .program_days_service import ProgramDayService
from .exercise_criteria_service import ExerciseCriteriaService
from .trainers_has_users_service import TrainerHasUserService
from .user_feedback_service import UserFeedbackService


users_service = UserService()
trainers_service = TrainerService()
programs_service = ProgramService()
exercise_service = ExerciseService()
program_assignment_service = ProgramAssignmentService()
programs_has_exercise_service = ProgramsHasExerciseService()
exercise_session_service = ExerciseSessionService()
program_days_service = ProgramDayService()
exercise_criteria_service = ExerciseCriteriaService()
trainers_has_users_service = TrainerHasUserService()