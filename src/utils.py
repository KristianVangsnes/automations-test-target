import os

AWS_ACCESS_KEY_ID = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
DATABASE_URL = os.getenv("DATABASE_URL")


def _require_env(name, value):
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def get_connection_string():
    return _require_env("DATABASE_URL", DATABASE_URL)


def get_aws_credentials():
    return (
        _require_env("AWS_ACCESS_KEY_ID", AWS_ACCESS_KEY_ID),
        _require_env("AWS_SECRET_ACCESS_KEY", AWS_SECRET_ACCESS_KEY),
    )
