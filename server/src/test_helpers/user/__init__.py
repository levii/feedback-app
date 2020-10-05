from typing import Optional

from common.user.domain.key import UserKey
from common.user.domain.user import User, UserName, CompanyName


def build_user(name: Optional[str] = None) -> User:
    return User(
        key=UserKey.build_new(),
        name=UserName(name or "John Smith"),
        company_name=CompanyName("New Company"),
    )
