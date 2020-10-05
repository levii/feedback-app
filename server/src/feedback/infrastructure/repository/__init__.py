from datetime import datetime, timezone
from typing import List, Dict

from injector import inject
from werkzeug.exceptions import NotFound

from common.user.domain.key import UserKey
from common.user.domain.user_repository import UserRepository
from feedback.domain.feedback import (
    Feedback,
    FeedbackUser,
    FeedbackTitle,
    FeedbackDescription,
    FeedbackStatus,
)
from feedback.domain.key import FeedbackKey
from feedback.domain.repository import FeedbackRepository


class InMemoryFeedbackRepository(FeedbackRepository):
    @inject
    def __init__(self, user_repository: UserRepository) -> None:
        self._user_repository = user_repository

        sample_feedbacks = [
            Feedback(
                key=FeedbackKey.build("f20001"),
                feedback_user=FeedbackUser.build_from_user(
                    user=self._user_repository.fetch_by_key(key=UserKey.build("c10001"))
                ),
                title=FeedbackTitle("要望サンプル"),
                description=FeedbackDescription("要望本文"),
                status=FeedbackStatus.New,
                created_at=datetime(2020, 10, 1, 10, 0, 0).astimezone(tz=timezone.utc),
            )
        ]

        self._feedbacks: Dict[FeedbackKey, Feedback] = {
            feedback.key: feedback for feedback in sample_feedbacks
        }

    def fetch_list(self) -> List[Feedback]:
        return list(self._feedbacks.values())

    def fetch_by_key(self, key: FeedbackKey) -> Feedback:
        feedback = self._feedbacks.get(key)
        if feedback:
            return feedback
        raise NotFound()

    def save(self, feedback: Feedback) -> None:
        self._feedbacks[feedback.key] = feedback
        return None
