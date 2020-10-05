import dataclasses
import datetime
import enum
from typing import List, Optional, Iterator, Iterable

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

    @classmethod
    def build(
        cls, feedback: Feedback, comments: Optional[FeedbackCommentCollection] = None
    ) -> "FeedbackWithComments":
        return cls(
            feedback=feedback, comments=comments or FeedbackCommentCollection([])
        )

    @property
    def key(self) -> FeedbackKey:
        return self.feedback.key

    @property
    def status(self) -> FeedbackStatus:
        return self.feedback.status

    def with_feedback(self, feedback: Feedback) -> "FeedbackWithComments":
        return self.build(feedback=feedback, comments=self.comments)


@dataclasses.dataclass(frozen=True)
class FeedbackCollection:
    _collection: List[Feedback]

    def __iter__(self) -> Iterator[Feedback]:
        return self._collection.__iter__()

    @classmethod
    def build(cls, feedbacks: Iterable[Feedback]) -> "FeedbackCollection":
        return cls(list(feedbacks))

    def append(self, feedback: Feedback) -> "FeedbackCollection":
        self._collection.append(feedback)
        return self

    def filter_by_user_key(self, user_key: UserKey) -> "FeedbackCollection":
        return self.build(
            [
                feedback
                for feedback in self
                if feedback.feedback_user.user_key == user_key
            ]
        )
