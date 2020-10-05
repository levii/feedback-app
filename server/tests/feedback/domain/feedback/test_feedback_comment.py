from feedback.domain.comment import (
    FeedbackComment,
    FeedbackCommentBody,
)
from test_helpers.feedback import build_feedback
from test_helpers.user import build_customer_user


class TestFeedbackComment:
    @classmethod
    def setup_class(cls):
        cls.feedback = build_feedback()

    def test_build_comment(self):
        comment = FeedbackComment.build_new(
            feedback_key=self.feedback.key,
            comment_user=build_customer_user(name="Comment User"),
            body=FeedbackCommentBody("要望コメント"),
        )
        assert isinstance(comment, FeedbackComment)
