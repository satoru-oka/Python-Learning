# 1行コメント
"""
複数行コメント
"""

# 改行時はバックスラッシュで連結
s = 'aaaaaaaaaa' \
    + 'bbbbbbbbb'
print(s)

# 改行時はパレンティスでも連結は可能
x = (1 + 1 + 1 + 1 + 1 + 1 + 1
    + 1 + 1 + 1 + 1 + 1 + 1 + 1)
print(x)
# 改行目安は80文字が良いらしい

x = 10
if x < 0:
    print('negative')
elif x == 0:
    print('zero')
elif x == 10:
    print('if文は始めに引っ掛かった方に制御が移る、10')
elif x == 10:
    print('if文はここの制御には移らない、10')
else:
    print('positive')

a = 5
b = 10

if a > 0:
    print('a is positive')
    if b > 0:
        print('b is positive')

# 比較演算子と論理演算子
a = 1
b = 1

# a が b と等しい
print(a == b)

# a が b　と異なる
print(a != b)

# a が b よりも小さい
print(a > b)

# a が b 以上である
print(a >= b)

# a も b も真であれば真
print(a > 0 and b > 0)

# a または b が真であれば真
print(a > 0 or b > 0)

# In と Not の使い所
y = [1, 2, 3]
x = 1

if x in y:
    print('in')

if 100 not in y:
    print('not in')

a = 1
b = 2

if not a == b:
    print('Not equal')

# 値が入っていない判定をするテクニック
# is_ok = True
# False, 0, 0.0, '', [], (), {}, set()
is_ok = [1, 2, 3, 4]

if is_ok:
    print('OK')
else:
    print('No!')

# Noneを判定する場合
is_empty = None
print(is_empty)
print(help(is_empty))

# 以下の記述は推奨されていない
if is_empty == None:
    print('None!!!')

# 以下の記述が推奨されている
if is_empty is not None:
    print('None!!!')
# is は objectを判定している
# print(1 == True)
# print(1 is True)

# while文とcontinue文とbreak文
print('##### while #####')
count = 0
while count < 5:
    print(count)
    count += 1

print('##### while break and continue #####')
count = 0
while True:
    if count >= 5:
        break

    if count == 2:
        count += 1
        continue

    print(count)
    count += 1

print('##### while else statement #####')
count = 0

while count < 5:
    # 条件を満たすとbreakによりループ処理から抜ける動作になる
    # if count == 1:
    # break
    print(count)
    count += 1
else:
    print('done')

# input method
# while True:
#     word = input('Enter:')
#     num = int(word)
#     if num == 100:
#         break
#     print('next')

# for statement
some_list = [1, 2, 3, 4, 5]

# i = 0
# while i < len(some_list):
#     print(some_list[i])
#     i += 1

# for i in some_list:
#     print(i)

for s in 'abcde':
    print(s)

for word in ['My', 'name', 'is', 'Mike']:
    if word == 'name':
        continue
    print(word)

# for else statement
for fruit in ['apple', 'banana', 'orange']:
    if fruit == 'banana':
        print('stop eating')
        break
    print(fruit)
else:
    print('I ate all!')

# range
for i in range(2, 10, 3):
    print(i)

for i in range(10):
    print(i, 'hello')

# _ を記述するとインデックスは使用しないと言う意味になる
for _ in range(10):
    print('hello')

# enumerate
for i, fruit in enumerate(['apple', 'banana', 'orange']):
    print(i, fruit)

# zip
days = ['Mon', 'Tue', 'Wed']
fruits = ['apple', 'banana', 'orange']
drinks = ['coffee', 'tea', 'beer']

# for i in range(len(days)):
    # print(days[i], fruits[i], drinks[i])

for day, fruit, drink, in zip(days, fruits, drinks):
    print(day, fruit, drink)

# dictionary for statement
d = {'x': 100, 'y': 200}
print(d.items())
for v in d.items():
    print(v)

# definition
def say_something():
    s = 'hi'
    return s

# 実行する際はパレンティスを記述する
print(type(say_something))
f =  say_something
f()

result = say_something()
print(result)

def what_is_this(color):
    if color == 'red':
        return 'tomato'
    elif color == 'green':
        return 'green papper'
    else:
        return "I don't know"

result = what_is_this('red')
result = what_is_this('green')
result = what_is_this('yellow')
print(result)

# 関数の引数と返り値の宣言
# [書式] 変数名: 整数型
num: int = 10

# 関数名(変数名: 整数型) -> 整数型
def add_num(a: int, b: int) -> int:
    return a + b

r = add_num(10, 20)
s = add_num('a', 'b')
print(r)
# pythonはデータ宣言と違う引数を渡してもエラーを起こさず値を返す
print(s)

# デフォルト引数で気をつけること
# 文字列、空のディクショナリ、リストなどは「None」で初期化。
# 参照渡しの動作が影響して思わぬバグになる
def test_func(x, l=None):
    if l is None:
        l = []
    l.append(x)
    return l

r = test_func(100)
print(r)

r = test_func(100)
print(r)

# 位置引数のタプル化
def say_something(word, *args):
    print('word =', word)
    for arg in args:
        print(arg)

# say_something('Hi!', 'Mike', 'Nance')
t = ('Mike', 'Nancy')
say_something('Hi!', *t)

# キーワード引数の辞書化
def menu(**kwargs):
    print(kwargs)
    for k, v in kwargs.items():
        print(k, v)

# menu(entree='beef', drink='coffee')

d = {
    'entree': 'beef',
    'drink': 'ice coffee',
    'dessert': 'ice'
}
menu(**d)
# Docstrings
def example_func(param1, param2):
    # pythonでは、関数内にドキュメントを記述する
    """Example function with types documented in the docstring

    Args:
        :param param1 (int): The first parameter.
        :param param2 (str: The second parameter.

        :return:
            bool: The return value. True for success, Fal^d^dse otherwise.
    """
    print(param1)
    print(param2)
    return True

# ドキュメント表示方法
print(example_func.__doc__)
print(help(example_func))

# inner function(関数内関数)
# 関数内で関数処理をしたい場合、他の関数では使用しないような時
def outer(a, b):

    def plus(c, d):
        return c + d

    r1 = plus(a, b)
    r2 = plus(b, a)
    print(r1 + r2)

outer(1, 2)

# closure
def outer(a, b):

    def inner():
        return a + b

    return inner

# closureを実行する為に変数に代入
f = outer(1, 2)

print('#####')

# closureを実行
r = f()
print(r)

def circle_area_func(pi):
    def circle_area(radius):
        return pi * radius * radius

    return circle_area

ca1 = circle_area_func(3.14)
ca2 = circle_area_func(3.141592)

print(ca1(10))
print(ca2(10))

# decorator
"""
デコレータとは高階関数を使用して既存の関数に対して機能を追加・変更するための機能です。
元の関数の処理内部に手を加えずに機能を追加・変更できるという点が大きなメリットです。
別ページで解説しますが、クラスにもデコレータを使用することができ、それらと区別する際は関数デコレータと呼びます。
"""
def print_more(func):
    def wrapper(*args, **kwargs):
        print('func:', func.__name__)
        print('args:', args)
        print('kwargs:', kwargs)
        result = func(*args, **kwargs)
        print('result:', result)
        return result
    return wrapper

def print_info(func):
    def wrapper(*args, **kwargs):
        print('start')
        result  =func(*args, **kwargs)
        print('end')
        return result
    return wrapper

@print_info
@print_more
def add_num(a, b):
    return a + b

r = add_num(10, 20)
print(r)

f = print_info(print_more(add_num))
r = f(10, 20)
print(r)

# lambda
l = ['Mon', 'tue', 'Wed', 'Thu', 'fri', 'sat', 'Sun']

def change_words(words, func):
    for word in words:
        print(func(word))

# def sample_func(word):
#     return word.capitalize()
#
# def sample_func2(word):
#     return word.lower()

# lambdaを使えば関数定義コードを記述しないで記述可能なのでコード量を抑えることが可能
change_words(l, lambda word: word.capitalize())
change_words(l, lambda word: word.lower())

# generators
l = ['Good morning', 'Good afternoon', 'Good night']

for i in l:
    print(i)

print('##########')

def greeting():
    yield 'Good morning'
    yield 'Good afternoon'
    yield 'Good night'

def counter(num=10):
    for _ in range(num):
        yield 'run'

g = greeting()
c = counter()

print(next(g))
print(next(c))
print("@@@@@")
print(next(g))
print("@@@@@")
print(next(g))

# リスト内包表記
t = (1, 2, 3, 4, 5)
t2 = (5, 6, 7, 8, 9, 10)

r = []
for i in t:
    if i % 2 == 0:
        r.append(i)

print(r)

# コードが簡潔、処理が早い
r = [i for i in t if i % 2 == 0]
print(r)

r = []
for i in t:
    for j in t2:
        r.append(i * j)
print(r)

r = [i * j for i in t for j in t2]

print(r)

# 辞書包括表記
w = ['mon', 'tue', 'wed']
f = ['coffee', 'milk', 'water']

d = {}
for x, y in zip(w, f):
    d[x] = y

print(d)

d = {x: y for x, y in zip(w, f)}
print(d)

# 集合内包表記
s = set()

for i in range(10):
    if i % 2 == 0:
        s.add(i)

print(s)

s = {i for i in range(10) if i % 2 == 0}
print(s)

# ジェネレーター内包表記
def g():
    for i in range(10):
        yield i

g = g()
print(next(g))

g = (i for i in range(10) if i % 2 == 0)
t = tuple(i for i in range(10))

for x in g:
    print(x)

print(t)

# namespace, scope
animal = 'cat'

def f():
    animal = 'dog'
    print('local:', locals())

f()
print('global:', globals())

# error handling
l = [1, 2, 3]
i = 5
del l

try:
    l[i]
# IndexErrorの場合にエラーハンドリング
except IndexError as ex:
    print("Don't worry: {}".format(ex))
except NameError as ex:
    print('other:{}'.format(ex))
# pythonでは全てのエラーをハンドリングすることは推奨されていない
except Exception as ex:
    print('other:{}'.format(ex))
# 例外処理に移らない場合の確認で使用することも可能。例外処理に問題ないことを確認するような使い方。
else:
    print('done')
finally:
    print('clean up')

print("last")

# 独自例外の作成
class UppercaseError(Exception):
    pass

def check():
    words = ['APPLE', 'orange', 'banana']
    for word in words:
        if word.isupper():
            raise UppercaseError(word)

try:
    check()
except UppercaseError as exc:
    print('This is my fault. Go next')