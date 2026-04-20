# 【例外処理の書き方】

### 複数の例外処理
try:
    # 1. 数値以外が入力されるリスク (ValueError)
    number = int(input("100を何で割りますか？ 整数を入力してください: "))
    
    # 2. 0が入力されるリスク (ZeroDivisionError)
    result = 100 / number

    print(f'計算結果: 100 ÷ {number} ⁼ {result}')
except ValueError:
    # int()変換に失敗した際（"abc"などが入力された時）の処理
    print("エラー: 整数を入力してください。")
except ZeroDivisionError:
    # 0で割ろうとした時の処理
    print("エラー: 0で割ることはできません。")
except Exception as e:
    print(f"予期せぬエラーが発生しました: {e}")