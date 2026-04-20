# 実践的なテストの作成と実行
from src.calc import add

def test_add():
    assert add(2, 3) == 5
    assert add(1, 1) == 2

from src.calc import add