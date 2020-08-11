import datetime


def utcnow_with_tz() -> datetime.datetime:
    return datetime.datetime.now(tz=datetime.timezone.utc)
