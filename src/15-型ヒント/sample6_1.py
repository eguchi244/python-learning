# 【型ヒントの使い方】

### 関数の型ヒント
name: str = "Taro"

def greet() -> str:
    return "こんにちは、" + name + "!"

# 下記は型違いのためエラーになる
# print(greet(20))

### リスト(list)の型ヒント
numbers: list[int] = [1, 2, 3]
names: list[str] = ['Alice', 'Bob', 'Charlie']

# print(numbers)
# print(names)

### 辞書(dict)の型ヒント
age_map: dict[str, int] = {'Alice': 30, 'Bob': 25, 'Charlie': 35}

# print(age_map)

### タプル(tuple)の型ヒント
coordinate: tuple[int, int] = (10, 20)
person: tuple[str, int, str] = ('Alice', 20, 'Enginieer')

# print(coordinate)
# print(person)

### セット(set)の型ヒント
unique_numbers: set[int] = {1, 2, 3, 2, 1}

print(unique_numbers)