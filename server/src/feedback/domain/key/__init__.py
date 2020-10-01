import dataclasses
import uuid
from typing import ClassVar, List


@dataclasses.dataclass(frozen=True)
class FeedbackKey:
    feedback_id: str

    KINDS: ClassVar[List[str]] = ["Feedback"]

    @classmethod
    def build(cls, feedback_id: str) -> "FeedbackKey":
        return cls(feedback_id)

    @classmethod
    def build_new(cls) -> "FeedbackKey":
        return cls.build(str(uuid.uuid4()))


@dataclasses.dataclass(frozen=True)
class FeedbackCommentKey:
    feedback_id: str
    comment_id: str

    KINDS: ClassVar[List[str]] = ["Feedback", "FeedbackComment"]

    @classmethod
    def build(cls, feedback_id: str, comment_id: str) -> "FeedbackCommentKey":
        return cls(feedback_id, comment_id)

    @classmethod
    def build_new(cls, feedback_key: FeedbackKey) -> "FeedbackCommentKey":
        return cls.build(
            feedback_id=feedback_key.feedback_id, comment_id=str(uuid.uuid4())
        )
