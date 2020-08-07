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


@dataclasses.dataclass(frozen=True)
class FeedbackDescription:
    value: str


@dataclasses.dataclass(frozen=True)
class Feedback:
    key: FeedbackKey
    feedback_user: FeedbackUser
    title: FeedbackTitle
    description: FeedbackDescription


@dataclasses.dataclass(frozen=True)
class FeedbackCollection:
    _collections: List[Feedback]
