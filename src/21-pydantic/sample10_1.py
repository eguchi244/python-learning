# 【基本的なモデルの定義】
from pydantic import BaseModel

class User(BaseModel):
    name: str
    age: int
    email: str

# 正常系
user = User(name="Taro", age=20, email="taro@example.com")

# 異常系
# user = User(name="Taro", age="二十歳", email="taro@example.com")

print(user.name)
print(user.email)
