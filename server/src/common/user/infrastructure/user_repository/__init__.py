from typing import List, Dict

from werkzeug.exceptions import NotFound

from common.user.domain.key import UserKey
from common.user.domain.user import User, UserName, CompanyName
from common.user.domain.user_repository import UserRepository


class InMemoryUserRepository(UserRepository):
    def __init__(self) -> None:
        sample_users = [
            User(
                key=UserKey("customer1"),
                name=UserName("顧客ユーザ1"),
                company_name=CompanyName("株式会社ラビィ"),
            ),
            User(
                key=UserKey("customer2"),
                name=UserName("顧客ユーザ2"),
                company_name=CompanyName("株式会社ラビィ"),
            ),
        ]

        self._users: Dict[UserKey, User] = {user.key: user for user in sample_users}

    def fetch_list(self) -> List[User]:
        return list(self._users.values())

    def fetch_by_key(self, key: UserKey) -> User:
        user = self._users.get(key)
        if user:
            return user
        raise NotFound()
