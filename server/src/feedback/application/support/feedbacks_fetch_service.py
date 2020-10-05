from injector import inject

from common.user.domain.user import SupportUser
from feedback.domain.feedback import FeedbackCollection
from feedback.domain.repository import FeedbackRepository


class FeedbacksFetchService:
    @inject
    def __init__(self, feedback_repository: FeedbackRepository):
        self._feedback_repository = feedback_repository

    def execute(self, user: SupportUser) -> FeedbackCollection:
        assert isinstance(user, SupportUser)
        feedbacks = self._feedback_repository.fetch_list()
        return feedbacks
