from typing import List

from feedback.domain.feedback import Feedback
from feedback.domain.key import FeedbackKey


class FeedbackRepository:
    def fetch_list(self) -> List[Feedback]:
        raise NotImplementedError()

    def fetch_by_key(self, key: FeedbackKey) -> Feedback:
        raise NotImplementedError()

    def save(self, feedback: Feedback) -> None:
        raise NotImplementedError()
