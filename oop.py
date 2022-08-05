# クラスの初期化とクラス変数
class Person(object):
    # 初期化処理、Personインスタンス生成時に初期化される - コンストラクタ
    def __init__(self, name):
        self.name = name
    # 引数にselfを指定し自クラスへアクセス
    def say_something(self):
        print('I am {}. hello'.format(self.name))
        self.run(10)

    def run(self, num):
        print('run' * num)
    # デストラクタ
    def __del__(self):
        print('good bye')

person = Person('Mike')
person.say_something()

# 明示的にデストラクタを呼び出す
del person

print('#############')

# # Inheritance
# class Car(object):
#     def run(self):
#         print('run')
#
# class ToyotaCar(Car):
#     pass
#
# class TeslaCar(Car):
#     def auto_run(self):
#         print('auto run')
#
# print('##########')
# toyota_car = ToyotaCar()
# toyota_car.run()
# print('##########')
# tesla_car = TeslaCar()
# # Car class
# tesla_car.run()
# # TeslaCar class
# tesla_car.auto_run()

# override & super class
# class Car(object):
#     def __init__(self, model=None):
#         self.model = model
#     def run(self):
#         print('run')
#
# class ToyotaCar(Car):
#     def run(self):
#         print('fast')
#
# class TeslaCar(Car):
#     def __init__(self, model='Model S', enable_auto_run=False):
#         super().__init__(model)
#         self.enable_auto_run = enable_auto_run
#
#     def run(self):
#         print('super fast')
#     def auto_run(self):
#         print('auto run')
#
# car = Car()
# car.run()
#
# print('##########')
# toyota_car = ToyotaCar('Lexus')
# print(toyota_car.model)
# toyota_car.run()
# print('##########')
# tesla_car = TeslaCar('Model S')
# print(tesla_car.model)
# # Car class
# tesla_car.run()
# # TeslaCar class
# tesla_car.auto_run()

# property
class Car(object):
    def __init__(self, model=None):
        self.model = model
    def run(self):
        print('run')

class ToyotaCar(Car):
    def run(self):
        print('fast')

class TeslaCar(Car):
    def __init__(self, model='Model S',
                 enable_auto_run=False,
                 passwd='123'):
        super().__init__(model)
        # 1. 参照されたくない場合、アンダースコア(_)唯、呼び出し側でアンダースコアを付けると呼び出せる。対策は、2を参照
        self.__enable_auto_run = enable_auto_run
        # 5
        self.passwd = passwd

    @property
    # 2. デコレータを付け以下の様に記述する。
    def enable_auto_run(self):
        return self._enable_auto_run

    @enable_auto_run.setter
    # 3. 書き換えを可能にする
    # 4. setterの使用例 5を参照
    def enable_auto_run(self, is_enable):
        # 5
        if self.passwd == '456':
            self._enable_auto_run = is_enable
        else:
            raise valueError

    def run(self):
        # 6. __ アンダースコアが2つの場合はクラス内のみアクセス可能
        print(self.__enable_auto_run)
        print('super fast')
    def auto_run(self):
        print('auto run')

tesla_car = TeslaCar('Model S', passwd='456')
tesla_car.run()
"""アンダースコアの種類
1. _ 書き換え不可を明示的にしているが、実際は書き換え可能　@プロパティを組み合わせ使用する。
2. __ 2つは、クラス内よりアクセスを可能とし、呼び出す際にはインスタンスを生成し呼び出す。1より厳格なルール
3. アンダースコア無しは、自由にアクセスが可能。
"""