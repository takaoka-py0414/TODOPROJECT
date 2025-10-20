# 栄養管理メモ (TODOPROJECT)

簡潔な説明  
日々の食事や気分（幸福度）を記録する Web アプリケーション（Django）。メモの登録・一覧・編集・削除、履歴、マイページ（ログイン必須）を提供します。

## デモ
- デモURL: （未設定）

## デモアカウント
- ユーザー名:  
- パスワード:   
（上の情報は実際のデプロイ時に設定してください。現在は空欄でも可）

## 要件定義
### 目的
- 利用者が日々の食事・気分を簡単に記録し、過去の傾向を確認できること。

### 対象ユーザー
- 一般ユーザー（個人の健康管理をしたい人）

### 機能要件（高レベル）
- ユーザー登録（アカウント作成）
- ログイン / ログアウト
- メモの新規作成（タイトル、メモ、幸福度、日付、カテゴリ等）
- メモ一覧表示（カテゴリ別の表示や簡易フィルタ）
- メモの編集・削除
- 日付ごとの履歴表示
- マイページ（ユーザー情報表示）

### 非機能要件
- 日本語 UI
- 開発段階は SQLite で動作
- モバイルフレンドリー（Bootstrap ベース）

## 機能一覧
- アカウント作成（UserCreationForm を使用）
- ログイン（AuthenticationForm）
- メモ一覧表示（朝食／昼食／夕食 などカテゴリ別）
- メモの作成・更新・削除（CRUD）
- 履歴（日時でグループ化して表示）
- マイページ（ログイン必須、ユーザー情報表示）

## 使用しているフレームワーク / ライブラリ
- Django（Python）
- Bootstrap 5（フロントエンド）
- Bootstrap Icons（アイコン、任意）
- （開発環境）SQLite（デフォルト DB）
- static/css/style.css にカスタムスタイルを追加

> 補足: 実際の requirements.txt がある場合はそちらを参照してください。例: Django==4.x, django-crispy-forms 等

## 外部 API
- 現状: なし

## ローカルでの起動手順（開発環境）
1. プロジェクトルートに移動（manage.py がある場所）
2. 仮想環境を作成・有効化（例・PowerShell）
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. 依存をインストール（requirements.txt がある場合）
   ```bash
   pip install -r requirements.txt
   ```
4. マイグレーション作成・適用
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```
5. 管理者（またはデモ）ユーザー作成（任意）
   
6. 開発サーバ起動
   ```bash
   python manage.py runserver
   ```
7. ブラウザでアクセス  
   http://127.0.0.1:8000/

## 備考（開発メモ）
- テンプレートは templates/ 配下、accounts, meal, products などのフォルダ構成。  
- マイグレーションに関する問題は `python manage.py showmigrations` で確認。

## ライセンス
- 指定がなければ自由に編集可能（必要なら適切なライセンスを追記してください）。