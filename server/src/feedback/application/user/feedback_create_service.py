from injector import inject

from common.user.domain.user import CustomerUser
from feedback.domain.feedback import Feedback, FeedbackTitle, FeedbackDescription
from feedback.domain.repository import FeedbackRepository


class FeedbackCreateService:
    @inject
    def __init__(self, feedback_repository: FeedbackRepository):
        self._feedback_repository = feedback_repository

    def execute(
        self, user: CustomerUser, title: FeedbackTitle, description: FeedbackDescription
    ) -> Feedback:
        feedback = Feedback.build_new(user=user, title=title, description=description)
        self._feedback_repository.save(feedback)
        return feedback
