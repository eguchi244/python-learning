"""
Chapter15-型ヒント
"""
# 【型ヒントの使い方】
### 変数への型ヒント
age: int = 20
name: str = 'Taro'

### 関数の型ヒント
def greet(name: str) -> str:
    return "こんにちは、" + name + "!"

print(greet('Jiro'))