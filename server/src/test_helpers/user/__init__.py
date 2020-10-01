from typing import Optional

from common.user.domain.key import UserKey
from common.user.domain.user import User, UserName, UserIconURL


def build_user(name: Optional[str] = None, icon_url: Optional[str] = None) -> User:
    return User(
        key=UserKey.build_new(),
        name=UserName(name or "John Smith"),
        icon_url=UserIconURL(icon_url or "http://example.com/user-icon.png"),
    )
