import dataclasses
from typing import List

from common.user.domain.key import UserKey
from common.user.domain.user import UserName, User
from feedback.domain.key import FeedbackCommentKey, FeedbackKey


@dataclasses.dataclass(frozen=True)
class FeedbackCommentUser:
    user_key: UserKey
    name: UserName

    @classmethod
    def build_from_user(cls, user: User) -> "FeedbackCommentUser":
        return cls(user_key=user.key, name=user.name)


@dataclasses.dataclass(frozen=True)
class FeedbackCommentBody:
    value: str


@dataclasses.dataclass(frozen=True)
class FeedbackComment:
    key: FeedbackCommentKey
    feedback_comment_user: FeedbackCommentUser
    body: FeedbackCommentBody

    @classmethod
    def build_new(
        cls, feedback_key: FeedbackKey, comment_user: User, body: FeedbackCommentBody
    ) -> "FeedbackComment":
        return cls(
            key=FeedbackCommentKey.build_new(feedback_key=feedback_key),
            feedback_comment_user=FeedbackCommentUser.build_from_user(
                user=comment_user
            ),
            body=body,
        )


@dataclasses.dataclass(frozen=True)
class FeedbackCommentCollection:
    _collection: List[FeedbackComment]

    @classmethod
    def build(cls, comments: List[FeedbackComment]) -> "FeedbackCommentCollection":
        return cls(comments)

    def append(self, comment: FeedbackComment) -> "FeedbackCommentCollection":
        self._collection.append(comment)
        return self
