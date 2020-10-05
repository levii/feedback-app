import dataclasses
import enum

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
class CompanyName:
    value: str

    MIN_LENGTH = 0
    MAX_LENGTH = 100

    def __post_init__(self) -> None:
        assert (
            len(self.value) >= self.MIN_LENGTH
        ), f"CompanyNameには長さ{self.MIN_LENGTH}以上の文字列を指定してください"
        assert (
            len(self.value) <= self.MAX_LENGTH
        ), f"CompanyNameには長さ{self.MAX_LENGTH}以下の文字列を指定してください"


class UserType(enum.Enum):
    Customer = "Customer"
    Support = "Support"


@dataclasses.dataclass(frozen=True)
class User:
    key: UserKey
    name: UserName
    user_type: UserType


@dataclasses.dataclass(frozen=True)
class CustomerUser(User):
    company_name: CompanyName

    TYPE = UserType.Customer

    @classmethod
    def build(
        cls, key: UserKey, name: UserName, company_name: CompanyName
    ) -> "CustomerUser":
        return cls(key=key, name=name, company_name=company_name, user_type=cls.TYPE)


@dataclasses.dataclass(frozen=True)
class SupportUser(User):
    TYPE = UserType.Support

    @classmethod
    def build(cls, key: UserKey, name: UserName) -> "SupportUser":
        return cls(key=key, name=name, user_type=cls.TYPE)
