import datetime
from typing import Optional, Union

from common.user.domain.user import User
from feedback.domain.feedback import (
    Feedback,
    FeedbackUser,
    FeedbackTitle,
    FeedbackDescription,
    FeedbackStatus,
)
from feedback.domain.key import FeedbackKey
from framework import utcnow_with_tz
from test_helpers.user import build_customer_user


def build_feedback(
    key: Optional[FeedbackKey] = None,
    feedback_user: Union[None, User, FeedbackUser] = None,
    title: Optional[str] = None,
    description: Optional[str] = None,
    status: Optional[FeedbackStatus] = None,
    now: Optional[datetime.datetime] = None,
) -> Feedback:
    if key is None:
        key = FeedbackKey.build_new()
    if feedback_user is None:
        feedback_user = FeedbackUser.build_from_user(user=build_customer_user())
    if isinstance(feedback_user, User):
        feedback_user = FeedbackUser.build_from_user(user=feedback_user)

    return Feedback(
        key=key,
        feedback_user=feedback_user,
        title=FeedbackTitle(title or "要望のタイトル"),
        description=FeedbackDescription(description or "要望の詳細"),
        status=status or FeedbackStatus.New,
        created_at=now or utcnow_with_tz(),
    )
