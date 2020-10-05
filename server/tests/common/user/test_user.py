import pytest

from common.user.domain.user import UserName, User, CompanyName
from test_helpers.user import build_customer_user


class TestUser:
    def test_valid_user_name(self):
        name = UserName("John Smith")
        assert isinstance(name, UserName)

    def test_invalid_too_short_user_name(self):
        with pytest.raises(AssertionError):
            UserName("ab")

    def test_invalid_too_long_user_name(self):
        with pytest.raises(AssertionError):
            UserName("a" * UserName.MAX_LENGTH + "x")

    def test_valid_company_name(self):
        company_name = CompanyName("Test Company")
        assert isinstance(company_name, CompanyName)

    def test_valid_empty_company_name(self):
        assert isinstance(CompanyName(""), CompanyName)

    def test_invalid_too_long_company_name(self):
        with pytest.raises(AssertionError):
            CompanyName("Very " + "." * CompanyName.MAX_LENGTH + " long name")

    def test_valid_user(self):
        user = build_customer_user(name="John One")
        assert isinstance(user, User)
        assert user.name == UserName("John One")
