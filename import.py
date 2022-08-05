# import文を記述する際には、標準、サードパーティー、自作パッケージ、ローカルファイル
# スペースを開けて区別できるようにすることが好ましい
# アルファベット順で記述が好まれる
import collections
import os
import sys

import termcolor

import call_test_package

import config

print(collections.__file__)
print(termcolor.__file__)
print(call_test_package.__file__)
print(config.__file__)

#　ローカルパッケージが優先的に読み込まれる
# 環境変数で出力されたパスのみパッケージは読み込まれる事に注意
# サードパーティーと同じパッケージを作るとローカルが優先して読み込まれるので、
# 注意しないと意図しない挙動になる
print(sys.path)