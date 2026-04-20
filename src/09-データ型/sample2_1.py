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