import dataclasses
from typing import List

from common.user.domain.key import UserKey
from common.user.domain.user import UserName, UserIconURL, User
from feedback.domain.key import FeedbackCommentKey


@dataclasses.dataclass(frozen=True)
class FeedbackCommentUser:
    user_key: UserKey
    name: UserName
    icon_url: UserIconURL

    @classmethod
    def build_from_user(cls, user: User) -> "FeedbackCommentUser":
        return cls(user_key=user.key, name=user.name, icon_url=user.icon_url)


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
