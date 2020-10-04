import dataclasses
import datetime
import enum
from typing import List

from common.user.domain.key import UserKey
from common.user.domain.user import User, UserName
from feedback.domain.comment import FeedbackCommentCollection
from feedback.domain.key import FeedbackKey
from framework import utcnow_with_tz


class FeedbackStatus(enum.Enum):
    New = "New"
    Accepted = "Accepted"
    Implementing = "Implementing"
    Released = "Released"
    WontFix = "WontFix"

    @classmethod
    def all_statuses(cls) -> List["FeedbackStatus"]:
        return [s for s in cls]


@dataclasses.dataclass(frozen=True)
class FeedbackUser:
    user_key: UserKey
    name: UserName

    @classmethod
    def build_from_user(cls, user: User) -> "FeedbackUser":
        return cls(user_key=user.key, name=user.name)


@dataclasses.dataclass(frozen=True)
class FeedbackTitle:
    value: str

    MIN_LENGTH = 1
    MAX_LENGTH = 200

    def __post_init__(self) -> None:
        assert (
            len(self.value) >= self.MIN_LENGTH
        ), f"FeedbackTitleには長さ{self.MIN_LENGTH}以上の文字列を指定してください"
        assert (
            len(self.value) <= self.MAX_LENGTH
        ), f"FeedbackTitleには長さ{self.MAX_LENGTH}以下の文字列を指定してください"


@dataclasses.dataclass(frozen=True)
class FeedbackDescription:
    value: str

    MIN_LENGTH = 1
    MAX_LENGTH = 10_000

    def __post_init__(self) -> None:
        assert (
            len(self.value) >= self.MIN_LENGTH
        ), f"FeedbackDescriptionには長さ{self.MIN_LENGTH}以上の文字列を指定してください"
        assert (
            len(self.value) <= self.MAX_LENGTH
        ), f"FeedbackDescriptionには長さ{self.MAX_LENGTH}以下の文字列を指定してください"


@dataclasses.dataclass(frozen=True)
class Feedback:
    key: FeedbackKey
    feedback_user: FeedbackUser
    title: FeedbackTitle
    description: FeedbackDescription
    status: FeedbackStatus
    created_at: datetime.datetime

    @classmethod
    def build_new(
        cls, user: User, title: FeedbackTitle, description: FeedbackDescription
    ) -> "Feedback":
        return cls(
            key=FeedbackKey.build_new(),
            feedback_user=FeedbackUser.build_from_user(user),
            title=title,
            description=description,
            status=FeedbackStatus.New,
            created_at=utcnow_with_tz(),
        )

    def with_status(self, status: FeedbackStatus) -> "Feedback":
        return Feedback(
            key=self.key,
            feedback_user=self.feedback_user,
            title=self.title,
            description=self.description,
            status=status,
            created_at=self.created_at,
        )


@dataclasses.dataclass(frozen=True)
class FeedbackWithComments:
    feedback: Feedback
    comments: FeedbackCommentCollection


@dataclasses.dataclass(frozen=True)
class FeedbackCollection:
    _collections: List[Feedback]
