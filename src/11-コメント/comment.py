"""
Chapter11-コメント
"""
# 【一行コメント】
# これはコメントです
print("Hello, world!")  # この後ろはコメントです

# 【複数行コメント】
"""
これは複数行コメントの例です
この部分もコメントになります
3行目のコメントです
"""

# 【アノテーションコメント】
"""
アノテーションコメントとは、注釈をコメントに付けることで、コメントの意図をわかりやすくするものです。
"""

### TODO
"""
用途
これから実装されるべき機能や、コードの改善点、追加すべきテストなど、まだ完了していないタスクを示すために使用されます。
"""
def calculate_average(scores):
    # TODO: ゼロ除算を考慮するエラーハンドリングを追加する
    return sum(scores) / len(scores)

### FIXME
"""
用途
コードにバグがあるか、あるいは期待通りに動作していない部分がある場合に使用します。
"""
def calculate_discount(price, discount):
    # FIXME: 割引率が負の値の場合に正しく計算されない
    return price - (price * discount)

### HACK
"""
用途
一時的な解決策や回避策をコードに適用した場合に使用します。
"""
# HACK: APIが空のリストを返すバグを回避する一時的な修正
def get_data():
    result = api_call()
    if result is None:
        return []  # 空のリストを返す
    return result
