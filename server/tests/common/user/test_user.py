import pytest

from common.user.domain.user import UserName, UserIcon


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
        icon = UserIcon("http://localhost/user-image.png")
        assert isinstance(icon, UserIcon)
        assert isinstance(UserIcon("https://example.com/user-image.png"), UserIcon)

    def test_invalid_starts_with_user_icon(self):
        with pytest.raises(AssertionError):
            UserIcon("test://example.com")

    def test_invalid_too_long_user_icon(self):
        with pytest.raises(AssertionError):
            UserIcon("http://example.com/" + "a" * UserIcon.MAX_LENGTH)

    def test_valid_user(self):
        pass
