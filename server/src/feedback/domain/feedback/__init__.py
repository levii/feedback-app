import dataclasses
from typing import List

from common.domain.key import UserKey
from feedback.domain.key import FeedbackKey


@dataclasses.dataclass(frozen=True)
class FeedbackUser:
    user_key: UserKey


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


@dataclasses.dataclass(frozen=True)
class FeedbackCollection:
    _collections: List[Feedback]
