"""
# 実践的なテストの作成と実行

必ず下記の直下に「conftest.py」（中身は空でOK）を配置すること
実施階層（ROOT）：C:/Users/Tsuyoshi/PythonProjects/python-learning/

必ず下記の階層で実施すること
実施階層（ROOT）：C:/Users/Tsuyoshi/PythonProjects/python-learning/

[tests/test_sample12_2.py]
from src.calc import add

def test_add():
    assert add(2, 3) == 5
    assert add(1, 1) == 2

from src.calc import add
"""
