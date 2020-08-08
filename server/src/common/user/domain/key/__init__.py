import dataclasses
import uuid
from typing import ClassVar, List


@dataclasses.dataclass(frozen=True)
class UserKey:
    user_id: str

    KINDS: ClassVar[List[str]] = ["User"]

    @classmethod
    def build(cls, user_id: str) -> "UserKey":
        return cls(user_id)

    @classmethod
    def build_new(cls) -> "UserKey":
        return cls.build(str(uuid.uuid4()))
