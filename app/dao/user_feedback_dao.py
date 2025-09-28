from .general_dao import GeneralDAO
from ..domain.user_feedback import UserFeedback  # Імпортуємо модель

class UserFeedbackDAO(GeneralDAO):
    _domain_type = UserFeedback  # Вказуємо тип домену (модель UserFeedback)

    # Метод для пошуку відгуків за користувачем (якщо необхідно)
    def find_by_id(self, feedback_id: int) -> UserFeedback:
        return UserFeedback.query.get(feedback_id)
