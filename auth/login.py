DEFAULT_USERNAME = "user"
DEFAULT_PASSWORD = "123"


def authenticate(username: str, password: str):

    return (
        username == DEFAULT_USERNAME
        and password == DEFAULT_PASSWORD
    )