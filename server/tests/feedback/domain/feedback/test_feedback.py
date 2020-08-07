from feedback.domain.feedback import FeedbackTitle


class TestFeedback:
    def test_valid_title(self):
        valid = FeedbackTitle("要望のタイトル")
        assert isinstance(valid, FeedbackTitle)
