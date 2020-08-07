import pytest

from feedback.domain.feedback import FeedbackTitle


class TestFeedback:
    def test_valid_title(self):
        valid = FeedbackTitle("要望のタイトル")
        assert isinstance(valid, FeedbackTitle)

    def test_invalid_empty_title(self):
        with pytest.raises(AssertionError):
            FeedbackTitle("")

    def test_invalid_too_long_title(self):
        with pytest.raises(AssertionError):
            FeedbackTitle("a" * FeedbackTitle.MAX_LENGTH + "x")
