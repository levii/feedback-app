from typing import List

from injector import inject

from common.user.domain.user import User
from feedback.domain.feedback import Feedback
from feedback.domain.repository import FeedbackRepository


class FeedbacksFetchService:
    @inject
    def __init__(self, feedback_repository: FeedbackRepository):
        self._feedback_repository = feedback_repository

    def execute(self, user: User) -> List[Feedback]:
        feedbacks = self._feedback_repository.fetch_list()

        return [
            feedback
            for feedback in feedbacks
            if feedback.feedback_user.user_key == user.key
        ]
