# 【環境変数の使い方】
from dotenv import load_dotenv
import os

### 環境変数の読み込み
PYENV_PATH = os.getenv('PYENV')
print(f'環境変数のパス: {PYENV_PATH}')

### 環境変数の設定
# 環境変数：コードには「変数名」だけ書き、中身はOSや外部ファイルから持ってくる
os.environ['NEW_VAR'] = 'value'
my_variable = os.getenv('NEW_VAR')
print(my_variable)

### .envファイルの読み込み
load_dotenv()

db_host = os.getenv('DB_HOST')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')

print(f'DBホスト: {db_host}, ユーザー: {db_user}, パスワード: {db_pass}')