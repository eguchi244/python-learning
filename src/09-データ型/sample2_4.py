# 【データ型(応用編)】
### 辞書型（Dictionary）

#1.辞書の作成
my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
print(f"1.辞書の作成: {my_dict}")

#2.要素へのアクセス
print(f"2.要素へのアクセス: {my_dict['name']}")

#3.要素の追加と変更
my_dict['email'] = 'john@example.com'  # 新しいキーと値の追加
my_dict['age'] = 31  # 既存のキーの値を変更
print(f"3.要素の追加と変更: {my_dict}")

#4.要素の削除
del my_dict['city']  # 'city'キーとその値を削除
print(f"4.要素の削除(del): {my_dict}")
my_dict.pop('name')  # これでも同様に削除できる
print(f"4.要素の削除(pop): {my_dict}")