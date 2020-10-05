from collections import defaultdict
from datetime import datetime, timezone
from typing import List, Dict

from injector import inject
from werkzeug.exceptions import NotFound

from common.user.domain.key import UserKey
from common.user.domain.user_repository import UserRepository
from feedback.domain.comment import FeedbackComment, FeedbackCommentCollection
from feedback.domain.feedback import (
    Feedback,
    FeedbackUser,
    FeedbackTitle,
    FeedbackDescription,
    FeedbackStatus,
    FeedbackWithComments,
    FeedbackCollection,
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

        self._comments: Dict[FeedbackKey, List[FeedbackComment]] = defaultdict(list)

    def fetch_list(self) -> FeedbackCollection:
        return FeedbackCollection.build(self._feedbacks.values())

    def fetch_by_key(self, key: FeedbackKey) -> FeedbackWithComments:
        feedback = self._feedbacks.get(key)
        if not feedback:
            raise NotFound()

        return FeedbackWithComments.build(
            feedback=feedback,
            comments=FeedbackCommentCollection.build(
                self._comments.get(feedback.key, [])
            ),
        )

    def save(self, feedback: Feedback) -> None:
        self._feedbacks[feedback.key] = feedback
        return None

    def save_comment(self, feedback_comment: FeedbackComment) -> None:
        self._comments[feedback_comment.feedback_key].append(feedback_comment)
        return None
