"""
Chapter09-データ型
"""
# 【代表的な型】
name = "Yamada Taro"  # 文字列
age = 20              # 整数
height = 170.5        # 浮動小数点数
is_student = True     # 真偽値

# 【データ型の変換】
# 下記は型不一致のエラーになる
# print('私は' + age + '歳です。')

# 修正版　strに型変換
print('私は' + str(age) + '歳です。')

# 【データ型(応用編)】
#　リスト（List）
my_list = [1, "Python", 3.14, [2, 4, 6]]

# タプル（Tuple）
my_tuple = (1, "Hello", 3.14)

# 辞書型（Dictionary）
my_dict = {"name": "John", "age": 30, "city": "New York"}

# セット(set)
my_set = {'apple', 'banana', 'cherry'}