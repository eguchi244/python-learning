# 【フォーマットの使い方】
import logging

# ログレベルをDEBUGに設定し、ログのフォーマットを定義します。
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(filename)s - %(message)s",
)

# ログメッセージを記録します。
logging.debug("デバッグ情報")
logging.info("情報メッセージ")
logging.warning("警告メッセージ")
logging.error("エラーメッセージ")
logging.critical("重大なエラーメッセージ")