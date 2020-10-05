from injector import inject

from common.user.domain.user import SupportUser
from feedback.domain.feedback import FeedbackWithComments
from feedback.domain.key import FeedbackKey
from feedback.domain.repository import FeedbackRepository


class FeedbackFetchService:
    @inject
    def __init__(self, feedback_repository: FeedbackRepository):
        self._feedback_repository = feedback_repository

    def execute(
        self, user: SupportUser, feedback_key: FeedbackKey
    ) -> FeedbackWithComments:
        assert isinstance(user, SupportUser)
        feedback = self._feedback_repository.fetch_by_key(key=feedback_key)
        return feedback
