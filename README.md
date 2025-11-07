# mealmanager

日々の食事や気分（幸福度）を記録する Web アプリケーション（Django）。メモの登録・一覧・編集・削除、履歴、マイページ（ログイン必須）を提供します。

## 🌐 本番デモ
**本番環境URL**: https://meal-manager-ewb7.onrender.com

すぐにお試しいただけるデモアカウント：
- **ユーザー名**: `demo`
- **パスワード**: `demopassword`

※ デプロイ時に自動作成されます

## デモ（開発環境）
以下のコマンドで、ローカル環境にデモユーザを追加できます。
```
DEMO_USER_EMAIL=demo@example.com DEMO_USER_PASSWORD=demopassword python manage.py create_demo_user
```

## 要件定義
### 目的
- 利用者が日々の食事・気分を簡単に記録し、過去の傾向を確認できること。

### 対象ユーザー
- 一般ユーザー（個人の健康管理をしたい人）

## 機能一覧
- **ユーザー管理**: 新規登録、ログイン/ログアウト
- **メモ機能**: 食事記録の作成・編集・削除（タイトル、メモ、幸福度、日付、カテゴリ）
- **表示機能**: カテゴリ別一覧表示、日付ごとの履歴表示
- **マイページ**: ログイン必須のユーザー情報表示
- **レスポンシブデザイン**: モバイル・PC両対応

## 使用しているフレームワーク / ライブラリ
- Django（Python）
- Bootstrap 5（フロントエンド）
- Bootstrap Icons（アイコン、任意）
- SQLite（データベース）
- WhiteNoise（静的ファイル配信）
- Gunicorn + Uvicorn（本番サーバー）
- static/css/style.css にカスタムスタイルを追加

## 環境設定
プロジェクトルートに `.env.example` ファイルが用意されています。実際の開発では以下の手順で環境変数を設定してください：

1. `.env.example` を `.env` にコピー
   ```bash
   cp .env.example .env
   ```

2. `.env` ファイルを編集し、実際の値を設定
   ```
   # Django
   SECRET_KEY=your_actual_secret_key_here
   DEBUG=True
   ALLOWED_HOSTS=localhost,127.0.0.1

   # デモ用（共有しても良いテストアカウント）
   DEMO_USER_EMAIL=demo@example.com
   DEMO_USER_PASSWORD=demopassword
   ```

> **注意**: `.env` ファイルは機密情報を含むため、Gitにコミットしないでください（.gitignoreに追加済み）。

## ローカルでの起動手順（開発環境）
1. プロジェクトルートに移動（manage.py がある場所）

2. 仮想環境作成・有効化
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   
   # 実行ポリシーは一時的に有効化
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope Process -Force
   ```

3. 依存関係をインストール
   ```bash
   pip install -r requirements.txt
   ```

4. マイグレーション作成・適用
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. デモユーザー作成（任意）
   ```bash
   python manage.py create_demo_user
   ```

6. 開発サーバ起動
   ```bash
   python manage.py runserver
   ```

7. ブラウザでアクセス  
   http://127.0.0.1:8000/

## 🚀 デプロイ
- **プラットフォーム**: Render.com
- **デプロイ方式**: GitHub連携による自動デプロイ
- **本番URL**: https://meal-manager-ewb7.onrender.com
- **本番データベース**: SQLite
- **自動化**: デモユーザー作成、静的ファイル収集、マイグレーション

## 📝 開発ポイント
- **テンプレート構造**: Django標準のテンプレート継承を活用
- **認証システム**: Django標準認証 + カスタムミドルウェア
- **レスポンシブ**: Bootstrap 5でモバイルファースト設計
- **デプロイ自動化**: GitHub連携による継続的デプロイメント