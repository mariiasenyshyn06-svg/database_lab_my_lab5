from ..dao.user_feedback_dao import UserFeedbackDAO
from .general_service import GeneralService
from app import db
from sqlalchemy import text
from ..domain.user_feedback import UserFeedback

class UserFeedbackService(GeneralService):
    _dao = UserFeedbackDAO()

    def create_feedback(self, user_id: int, trainer_id: int, feedback_text: str, rating: int):
        db.session.execute(
            text("CALL insert_user_feedback(:user_id, :trainer_id, :feedback_text, :rating)"),
            {'user_id': user_id, 'trainer_id': trainer_id, 'feedback_text': feedback_text, 'rating': rating}
        )
        db.session.commit()

        # Створює об'єкт UserFeedback
        feedback = UserFeedback(
            user_id=user_id,
            trainer_id=trainer_id,
            feedback_text=feedback_text,
            rating=rating
        )

        return feedback.put_into_dto()
