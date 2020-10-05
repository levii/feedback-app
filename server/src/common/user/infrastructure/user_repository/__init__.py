from typing import List, Dict

from werkzeug.exceptions import NotFound

from common.user.domain.key import UserKey
from common.user.domain.user import (
    User,
    UserName,
    CompanyName,
    CustomerUser,
    SupportUser,
)
from common.user.domain.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        sample_users = [
            CustomerUser.build(
                key=UserKey("c10001"),
                name=UserName("山田 太郎"),
                company_name=CompanyName("株式会社ラビィ"),
            ),
            CustomerUser.build(
                key=UserKey("c10002"),
                name=UserName("山田 次郎"),
                company_name=CompanyName("株式会社ラビィ"),
            ),
            SupportUser.build(key=UserKey("s90099"), name=UserName("佐藤 健太"),),
        ]

        self._users: Dict[UserKey, User] = {user.key: user for user in sample_users}

    def fetch_list(self) -> List[User]:
        return list(self._users.values())

    def fetch_by_key(self, key: UserKey) -> User:
        user = self._users.get(key)
        if user:
            return user
        raise NotFound()
