# 【同期処理と非同期処理の比較】
### 同期処理の場合

import time

def task1():
    print("Task 1 started")
    time.sleep(2)  # 2秒間処理をブロック
    print("Task 1 completed")

def task2():
    print("Task 2 started")
    time.sleep(2)  # 2秒間処理をブロック
    print("Task 2 completed")

def main():
    task1()
    task2()

main()