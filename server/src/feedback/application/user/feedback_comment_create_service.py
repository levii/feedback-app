from injector import inject

from common.user.domain.user import User
from feedback.domain.comment import FeedbackCommentBody, FeedbackComment
from feedback.domain.key import FeedbackKey
from feedback.domain.repository import FeedbackRepository


class FeedbackCommentCreateService:
    @inject
    def __init__(self, feedback_repository: FeedbackRepository):
        self._feedback_repository = feedback_repository

    def execute(
        self,
        user: User,
        feedback_key: FeedbackKey,
        feedback_comment_body: FeedbackCommentBody,
    ) -> FeedbackComment:
        feedback_comment = FeedbackComment.build_new(
            feedback_key=feedback_key, comment_user=user, body=feedback_comment_body
        )
        self._feedback_repository.save_comment(feedback_comment)
        return feedback_comment
