# 【if文 - 条件による分岐】
"""
# 18未満は未成年
# 18以上-65未満は成人
# それ以外は高齢者
"""
age = 20

if age < 18:
    print('未成年です。')
elif age >= 18 and age < 65:
    print('成人です。')
else:
    print('高齢者です。')