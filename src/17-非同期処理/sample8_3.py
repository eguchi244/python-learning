# 【同期処理と非同期処理の比較】
### 非同期の場合

import asyncio

async def task1():
    print("Task 1 started")
    await asyncio.sleep(2)  # 非同期で2秒間待機
    print("Task 1 completed")

async def task2():
    print("Task 2 started")
    await asyncio.sleep(2)  # 非同期で2秒間待機
    print("Task 2 completed")

async def main():
    await asyncio.gather(task1(), task2())  # task1とtask2を同時に実行

asyncio.run(main())
