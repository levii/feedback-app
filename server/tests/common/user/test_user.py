import pytest

from common.user.domain.user import UserName, UserIconURL, User
from test_helpers.user import build_user


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

    def test_valid_user_icon(self):
        icon = UserIconURL("http://localhost/user-image.png")
        assert isinstance(icon, UserIconURL)
        assert isinstance(
            UserIconURL("https://example.com/user-image.png"), UserIconURL
        )

    def test_invalid_starts_with_user_icon(self):
        with pytest.raises(AssertionError):
            UserIconURL("test://example.com")

    def test_invalid_too_long_user_icon(self):
        with pytest.raises(AssertionError):
            UserIconURL("http://example.com/" + "a" * UserIconURL.MAX_LENGTH)

    def test_valid_user(self):
        user = build_user(name="John One")
        assert isinstance(user, User)
        assert user.name == UserName("John One")
