"""
Chapter20-DocStringによるドキュメンテーション
"""
# 【DocStringとは？】
"""
DocStringとは？
DocString（ドキュメント文字列）は、関数、クラス、モジュールの最初に書かれる文字列で、そのコードブロックが何をするのかを説明します。
Pythonでは、三重クォートを使用してDocstringを書きます。
これにより、他のプログラマーがあなたのコードをより簡単に理解し、使い方をすぐに把握できるようになります。
"""

# 【Docstringの書き方】
def add(a: int, b: int) -> int:
    """
    二つの数値を加算するメソッド

    Args:
        a (int): 数値1
        b (int): 数値2

    Returns:
        int: aとbの合計値
    """
    return a + b