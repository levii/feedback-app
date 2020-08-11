from feedback.domain.comment import (
    FeedbackComment,
    FeedbackCommentUser,
    FeedbackCommentBody,
)
from feedback.domain.key import FeedbackCommentKey
from test_helpers.feedback import build_feedback
from test_helpers.user import build_user


class TestFeedbackComment:
    @classmethod
    def setup_class(cls):
        cls.feedback = build_feedback()

    def test_build_comment(self):
        comment = FeedbackComment(
            key=FeedbackCommentKey.build_new(feedback_key=self.feedback.key),
            feedback_comment_user=FeedbackCommentUser.build_from_user(
                user=build_user(name="Comment User")
            ),
            body=FeedbackCommentBody("要望コメント"),
        )
        assert isinstance(comment, FeedbackComment)
