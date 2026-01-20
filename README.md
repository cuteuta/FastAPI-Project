# FastAPI TODO API

## 概要
FastAPIを用いて作成したシンプルなTODO管理APIです。
未経験からの学習を目的に、最小構成から段階的に機能追加しました。

## 機能
- タスク一覧取得（GET /tasks）
- タスク追加（POST /tasks）
- タスク削除（DELETE /tasks/{id}）
- SQLiteによるデータ永続化

## 技術スタック
- Python
- FastAPI
- SQLite
- Uvicorn

## 工夫した点
- 最初はメモリ上で実装し、その後SQLiteに置き換えることで段階的に改善しました
- Pydanticを用いて入力データのバリデーションを行いました
- Swagger UIを活用し、APIの動作確認を容易にしました

## 起動方法
```bash
pip install fastapi uvicorn
uvicorn main:app --reload
