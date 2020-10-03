from typing import List

from common.user.domain.key import UserKey
from common.user.domain.user import User


class UserRepository:
    def fetch_list(self) -> List[User]:
        raise NotImplementedError()

    def fetch_by_key(self, key: UserKey) -> User:
        raise NotImplementedError()
