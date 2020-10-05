from injector import inject
from werkzeug.exceptions import Forbidden

from common.user.domain.user import User
from feedback.domain.feedback import Feedback
from feedback.domain.key import FeedbackKey
from feedback.domain.repository import FeedbackRepository


class FeedbackFetchService:
    @inject
    def __init__(self, feedback_repository: FeedbackRepository):
        self._feedback_repository = feedback_repository

    def execute(self, user: User, feedback_key: FeedbackKey) -> Feedback:
        feedback = self._feedback_repository.fetch_by_key(key=feedback_key)
        if self._permission_check(user=user, feedback=feedback):
            return feedback

        raise Forbidden()

    def _permission_check(self, user: User, feedback: Feedback) -> bool:
        return feedback.feedback_user.user_key == user.key
