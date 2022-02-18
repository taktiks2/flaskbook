import os
import shutil
import pytest
from apps.crud.models import db, User
from apps.app import create_app
from apps.detector.models import UserImage, UserImageTag


# フィクスチャ関数を作成
@pytest.fixture
def fixture_app():
    # セットアップ処理
    # テスト用のコンフィグを使うために引数にtestingを指定
    app = create_app("testing")

    # データベースを利用するための宣言
    app.app_context().push()

    # テスト用データベースのテーブルを作成
    with app.app_context():
        db.create_all()

    # テスト用の画像アップロードディレクトリを作成
    os.mkdir(app.config["UPLOAD_FOLDER"])

    # テストを実行
    yield app

    # クリーンナップ処理
    # userテーブルのレコードを削除
    User.query.delete()

    # user_imageテーブルのレコードを削除
    UserImage.query.delete()

    # user_image_tagsテーブルのレコードを削除
    UserImageTag.query.delete()

    # テスト用の画像アップロードディレクトリを削除
    shutil.rmtree(app.config["UPLOAD_FOLDER"])

    db.session.commit()


# Flaskのテストクライアントを返すフィクスチャ関数を作成
@pytest.fixture
def client(fixture_app):
    # Flaskのテスト用クライアントを返す
    return fixture_app.test_client()
