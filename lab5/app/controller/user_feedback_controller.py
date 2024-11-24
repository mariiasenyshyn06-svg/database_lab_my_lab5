from .general_controller import GeneralController
from ..service.user_feedback_service import UserFeedbackService
from flask_restful import Resource

class UserFeedbackController(GeneralController, Resource):
    _service = UserFeedbackService()  # ініціалізуємо сервіс тут

    def create_feedback(self, user_id: int, trainer_id: int, feedback_text: str, rating: int):
        # Створює новий відгук через сервіс і повертає DTO
        feedback_dto = self._service.create_feedback(user_id, trainer_id, feedback_text, rating)
        return feedback_dto
