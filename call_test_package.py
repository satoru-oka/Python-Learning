# import test_package.utils
# 使用できるが読み難い為、推奨されていない
# from ..tools import utils
from test_package.tools import utils
# from test_package.utils import say_twice
# 多用はあまりしない方が良い記述
# from test_package.talk import  utils as a
from test_package.talk import human
from test_package.talk import animal
# __init__ で [animal]を認識できるように初期化すれば以下の記述でも可能。
# どんなモジュールが使われるか分からない為、推奨されていない。
# from test_package.talk import *
# ImportErrorの使い所
try:
    from test_package import utils
except ImportError:
    from test_package.tools import utils

utils.say_twice('word')


print(animal.sing())

# r = test_package.utils.say_twice('hello')
r = utils.say_twice('hello')
# r =  say_twice('hello')

print(r)

print(human.sing())
print(human.cry())
