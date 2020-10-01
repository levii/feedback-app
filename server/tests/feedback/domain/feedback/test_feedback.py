import pytest

from feedback.domain.feedback import FeedbackTitle, FeedbackDescription, Feedback
from test_helpers.feedback import build_feedback


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

    def test_valid_description(self):
        valid = FeedbackDescription("要望の本文")
        assert isinstance(valid, FeedbackDescription)

    def test_invalid_empty_description(self):
        with pytest.raises(AssertionError):
            FeedbackDescription("")

    def test_invalid_too_long_description(self):
        with pytest.raises(AssertionError):
            FeedbackDescription("a" * FeedbackDescription.MAX_LENGTH + "x")

    def test_build_feedback(self):
        feedback = build_feedback()
        assert isinstance(feedback, Feedback)
