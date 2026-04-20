# 【テストの作成】
def func(x: int) -> int:
    return x + 1

def test_answer():
    assert func(3) == 4
    # assert func(3) == 3