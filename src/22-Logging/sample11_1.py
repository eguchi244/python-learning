# 【Loggingの使い方】
import logging

logging.basicConfig(level=logging.INFO)

logging.debug('これはデバッグメッセージです。')
logging.info('これは情報メッセージです。')
logging.warning('これは警告メッセージです。')
logging.error('これはエラーメッセージです。')
logging.critical('これはクリティカルメッセージです。')