# 【match文 - パターンマッチング】
# リストとパターンの組み合わせ
# command = ["start", 10]
# command = ["stop"]
command = ["pause", 10]

match command:
        case ["start", params]:
            print(f"スタートコマンドが実行されました。パラメータ: {params}")
            # スタートコマンドの処理をここに実装
        case ["stop"]:
            print("ストップコマンドが実行されました。")
            # ストップコマンドの処理をここに実装
        case ["pause", duration]:
            print(f"一時停止コマンドが実行されました。期間: {duration}秒")
            # 一時停止コマンドの処理をここに実装
        case _:
            print("無効なコマンドです。")
            # 無効なコマンドの処理をここに実装