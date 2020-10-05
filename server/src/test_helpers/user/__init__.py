from typing import Optional

from common.user.domain.key import UserKey
from common.user.domain.user import UserName, CompanyName, CustomerUser


def build_customer_user(name: Optional[str] = None) -> CustomerUser:
    return CustomerUser.build(
        key=UserKey.build_new(),
        name=UserName(name or "John Smith"),
        company_name=CompanyName("New Company"),
    )
