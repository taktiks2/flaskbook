from pathlib import Path

basedir = Path(__file__).parent.parent


class BaseConfig:
    SECRET_KEY = "slkFgWiosfweoi35dkdfoDD"
    WTF_CSRF_SECRET_KEY = "laugehSREEeeer3rj"


class LocalConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'local.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True


class TestingConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = f"sqlite:///{basedir / 'testing.sqlite'}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False


config = {
    "testing": TestingConfig,
    "local": LocalConfig,
}
