import dataclasses
from typing import List

from common.user.domain.key import UserKey
from feedback.domain.key import FeedbackCommentKey


@dataclasses.dataclass(frozen=True)
class FeedbackCommentUser:
    user_key: UserKey


@dataclasses.dataclass(frozen=True)
class FeedbackCommentBody:
    value: str


@dataclasses.dataclass(frozen=True)
class FeedbackComment:
    key: FeedbackCommentKey
    feedback_comment_user: FeedbackCommentUser
    body: FeedbackCommentBody


@dataclasses.dataclass(frozen=True)
class FeedbackCommentCollection:
    _collection: List[FeedbackComment]
