AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"

DATABASE_URL = "postgresql://admin:supersecret@prod-db.internal:5432/myapp"


def get_connection_string():
    return DATABASE_URL


def get_aws_credentials():
    return AWS_ACCESS_KEY, AWS_SECRET_KEY
