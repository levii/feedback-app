# DDD Sample Feedback Python App

## Setup

### Python venv 環境作成

Python3.8 を利用して、venv 環境を作成してください。

```
$ python -m venv venv
$ source venv/bin/activate
```

必要ならば、 direnv などを使って、ディレクトリに移動した際に自動で activate されるように設定してください。

```
$ direnv edit
# -->  source venv/bin/activate と記載
$ direnv allow .
```

### 依存ライブラリのインストール

venv 環境が activate されている状態で、以下のコマンドを実行してください。

```
$ pip install -r server/src/requirements.dev.txt
```

本番サーバ環境で必要なライブラリについては `server/src/requirements.in` に、開発環境でのみ必要なライブラリについては `server/src/requirements.dev.in` に追加してください。
その後、依存ライブラリのバージョンを固定するために、 `make pip-compile` コマンドを実行します。

```
$ vi server/src/requirements.in
$ vi server/src/requirements.dev.in

$ make pip-compile
$ pip install -r server/src/requirements.dev.txt
```

### デモ用の起動

一連の操作をデモンストレーションする場合には、自動リロードが行われないように、以下のようにサーバを起動してください。

```
$ cd server
$ make demo-server
```

(ソースコード変更を検知して再読み込みが行われると、 InMemoryRepository の内容がクリアされます。)
