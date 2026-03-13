import os


def _require_env(name):
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


AWS_ACCESS_KEY = _require_env("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = _require_env("AWS_SECRET_ACCESS_KEY")
DATABASE_URL = _require_env("DATABASE_URL")


def get_connection_string():
    return DATABASE_URL


def get_aws_credentials():
    return AWS_ACCESS_KEY, AWS_SECRET_KEY
