# app/dao/__init__.py

from .users_dao import UserDAO
from .trainers_dao import TrainerDAO
from .programs_dao import ProgramDAO
from .exercise_dao import ExerciseDAO
from .program_assignment_dao import ProgramAssignmentDAO
from .programs_has_exercise_dao import ProgramsHasExerciseDAO
from .exercise_session_dao import ExerciseSessionDAO
from .program_days_dao import ProgramDayDAO
from .exercise_criteria_dao import ExerciseCriteriaDAO
from .trainers_has_users_dao import TrainerHasUserDAO
from .user_feedback_dao import UserFeedbackDAO

# Імпортуємо всі DAO тут, щоб їх можна було використовувати у сервісах і контролерах
users_dao = UserDAO()
trainers_dao = TrainerDAO()
programs_dao = ProgramDAO()
exercise_dao = ExerciseDAO()
program_assignment_dao = ProgramAssignmentDAO()
programs_has_exercise_dao = ProgramsHasExerciseDAO()
exercise_session_dao = ExerciseSessionDAO()
program_days_dao = ProgramDayDAO()
exercise_criteria_dao = ExerciseCriteriaDAO()
trainers_has_users_dao = TrainerHasUserDAO()
user_feedback_dao = UserFeedbackDAO()