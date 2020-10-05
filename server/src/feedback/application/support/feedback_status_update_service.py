from injector import inject

from common.user.domain.user import SupportUser
from feedback.domain.feedback import FeedbackWithComments, FeedbackStatus
from feedback.domain.key import FeedbackKey
from feedback.domain.repository import FeedbackRepository


class FeedbackStatusUpdateService:
    @inject
    def __init__(self, feedback_repository: FeedbackRepository):
        self._feedback_repository = feedback_repository

    def execute(
        self, user: SupportUser, feedback_key: FeedbackKey, status: FeedbackStatus
    ) -> FeedbackWithComments:
        assert isinstance(user, SupportUser)
        feedback = self._feedback_repository.fetch_by_key(key=feedback_key)
        modified_status = feedback.feedback.with_status(status=status)
        self._feedback_repository.save(modified_status)
        return feedback.with_feedback(feedback=modified_status)
