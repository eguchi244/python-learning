# 【match文 - パターンマッチング】
# 単純な値のマッチング
status_code = 404

match status_code:
    case 200:
        print("成功!")
    case 404:
        print("見つかりません。")
    case _:
        print("その他のエラー。")
