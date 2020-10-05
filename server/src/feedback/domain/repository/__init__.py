from feedback.domain.comment import FeedbackComment
from feedback.domain.feedback import Feedback, FeedbackWithComments, FeedbackCollection
from feedback.domain.key import FeedbackKey


class FeedbackRepository:
    def fetch_list(self) -> FeedbackCollection:
        raise NotImplementedError()

    def fetch_by_key(self, key: FeedbackKey) -> FeedbackWithComments:
        raise NotImplementedError()

    def save(self, feedback: Feedback) -> None:
        raise NotImplementedError()

    def save_comment(self, feedback_comment: FeedbackComment) -> None:
        raise NotImplementedError()
