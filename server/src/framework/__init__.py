import datetime


def utcnow_with_tz():
    return datetime.datetime.now(tz=datetime.timezone.utc)
