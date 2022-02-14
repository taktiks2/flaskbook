from pathlib import Path

basedir = Path(__file__).parent.parent


class BaseConfig:
    SECRET_KEY = "slkFgWiosfweoi35dkdfoDD"
    WTF_CSRF_SECRET_KEY = "laugehSREEeeer3rj"
    # 画像のアップロード先を指定
    UPLOAD_FOLDER = str(Path(basedir, "apps", "images"))


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
