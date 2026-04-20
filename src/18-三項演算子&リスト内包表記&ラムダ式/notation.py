"""
Chapter18-三項演算子 & リスト内包表記 & ラムダ式
"""
# 【Pythonの便利な表記法】
### 三項演算子（条件式）
"""
値1 if 条件 else 値2
"""
# 三項演算子を使った例
x = 20
result = '偶数' if x % 2 == 0 else '奇数'
print(result)

# 三項演算子を使わなかった例
x = 20
result = ''
if x % 2 == 0:
    result = '偶数'
else:
    result = '奇数'
print(result)

### リスト内包表記
"""
[式 for アイテム in イテラブル(リスト、タプル、辞書など)if 条件]
"""
# リスト内包表記を使った例
squares = [x**2 for x in range(10)]
print(squares)

# リスト内包表記を使わない例
squares: list[int] =[]
for x in range(10):
    squares.append(x**2)
print(squares)

### ラムダ式
"""
lambda 引数: 式
"""
# ラムダ式を使った例
add = lambda x, y: x + y
print(add(1,2))

#
def add(x: int, y: int) -> int:
    return x + y
print(add(1,2))