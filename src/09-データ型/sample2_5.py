# 【データ型(応用編)】
### セット(set)

#1.セットの作成
my_set = {'apple', 'banana', 'cherry'}
print(f"1.セットの作成: {my_set}")

#2.要素の追加
my_set.add('orange')
print(f"2.要素の追加(1回目): {my_set}")
my_set.add('orange')
print(f"2.要素の追加(2回目): {my_set}")

#3.要素の削除
my_set.remove('banana')
print(f"3.要素の削除: {my_set}")