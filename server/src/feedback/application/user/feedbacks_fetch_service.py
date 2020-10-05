from injector import inject

from common.user.domain.user import CustomerUser
from feedback.domain.feedback import FeedbackCollection
from feedback.domain.repository import FeedbackRepository


class FeedbacksFetchService:
    @inject
    def __init__(self, feedback_repository: FeedbackRepository):
        self._feedback_repository = feedback_repository

    def execute(self, user: CustomerUser) -> FeedbackCollection:
        feedbacks = self._feedback_repository.fetch_list()

        return FeedbackCollection.build(
            [
                feedback
                for feedback in feedbacks
                if feedback.feedback_user.user_key == user.key
            ]
        )
