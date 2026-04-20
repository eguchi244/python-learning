# 【クラスの定義と使用方法】
### クラスの定義
class Person:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"こんにちは！, 私は {self.name} です。年齢は {self.age} 歳です。")

### クラスの使用例

#Personクラスのインスタンスを生成
person1 = Person("太郎", 30)

# インスタンスのメソッドを呼び出し
person1.greet()
