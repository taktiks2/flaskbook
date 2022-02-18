# 未ログイン時
def test_index(client):
    rv = client.get("/")
    assert "ログイン" in rv.data.decode()
    assert "画像新規登録" in rv.data.decode()


def signup(client, username, email, password):
    """サインアップする"""
    data = dict(username=username, email=email, password=password)
    return client.post("/auth/signup", data=data, follow_redirects=True)


# ログイン時
def test_index_signup(client):
    """サインアップの実行"""
    rv = signup(client, "admin", "flaskbook@example.com", "password")
    assert "admin" in rv.data.decode()

    rv = client.get("/")
    assert "ログアウト" in rv.data.decode()
    assert "画像新規登録" in rv.data.decode()
