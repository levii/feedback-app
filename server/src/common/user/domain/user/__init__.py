import dataclasses
import re

from common.user.domain.key import UserKey


@dataclasses.dataclass(frozen=True)
class UserName:
    value: str

    MIN_LENGTH = 3
    MAX_LENGTH = 30

    def __post_init__(self) -> None:
        assert (
            len(self.value) >= self.MIN_LENGTH
        ), f"UserNameには長さ{self.MIN_LENGTH}以上の文字列を指定してください"
        assert (
            len(self.value) <= self.MAX_LENGTH
        ), f"UserNameには長さ{self.MAX_LENGTH}以下の文字列を指定してください"


@dataclasses.dataclass(frozen=True)
class UserIcon:
    value: str

    URL_PATTERN = r"https?://"
    MAX_LENGTH = 200

    def __post_init__(self) -> None:
        assert re.match(
            self.URL_PATTERN, self.value
        ), f"UserNameの値は{self.URL_PATTERN}に合致する文字列を指定してください"
        assert (
            len(self.value) <= self.MAX_LENGTH
        ), f"UserNameには長さ{self.MAX_LENGTH}以下の文字列を指定してください"


@dataclasses.dataclass(frozen=True)
class User:
    key: UserKey
    name: UserName
    icon: UserIcon
