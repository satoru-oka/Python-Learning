# List
r = [1, 2, 3, 4, 5, 1, 2, 3]
print(r.index(3, 3))

print(r.count(3))

if 5 in r:
    print('exist')

r.sort()
print(r)
r.sort(reverse=True)
print(r)
r.reverse()
print(r)

s = 'My name is Mike.'
print(s)
to_split = s.split(' ')
print(to_split)

x = ' ###### '.join(to_split)
print(x)

# print(help(list))

# list copy
i = [1, 2, 3, 4, 5]
j = i
j[0] = 100
print('j =', j)
print('i =', i)

x = [1, 2, 3, 4, 5]
y = x.copy()
# y = x[:]
print('y =', y)
y[0] = 100
print('y =', y)
print('x =', x)

X = 20
Y = X
Y = 5
print(id(X))
print(id(Y))
print(Y)
print(X)

X = ['a', 'b']
Y = X
print(X)
print(Y)
Y[0] = 'p'
print(id(X))
print(id(Y))
print(Y)
print(X)
# TODO: 202207/01~03, Python Environment Set up, Python basic, Data Structure
# 202207/01 Python Data Structure tuple type
# tuple unpacking
print('########### tuple unpacking ###########')
num_tuple = (10, 20)
print(num_tuple)

x, y = num_tuple
print(x, y)

x, y = 10, 20
print(x, y)

min, max = 0, 100
print(min, max)

# プログラムが長すぎると読み難い為、好ましくない
a, b, c, d, e, f = 'Mike', '1', '1', '1', 'e', 'f'
a = 'Mike'
b = '1'

# 冗長なコード
print('##### 冗長なコード #####')
i = 100
j = 200
tmp = i
i = j
j = tmp
print(i, j)

# unpacking
print('##### unpacking #####')
a = 100
b = 200
print(a, b)
a, b = b, a
print(a, b)

# tuple使い所
# chose_from_two = ('A', 'B', 'C')
# chose_from_two = ['A', 'B', 'C']

answer = []

# tupleは、値を追加することができない。その特徴を活用したアプリケーションの実装を考える。
# chose_from_two.append('A')
# chose_from_two.append('C')

# print(chose_from_two)
print(answer)

# dictionary copy
print('##### dictionary copy #####')
x = {'a': 1}
y = x
y['a'] = 1000
# yはxのアドレスの先頭を参照している状態
print(x)
print(y)

# 辞書型の使い所
# list
l = [
    ['apple', 100],
    ['banana', 200],
    ['orange', 300],
]
print(l[0])

# dictionary データ構造がハッシュテーブルなのでリストより高速処理が可能
fruits = {
    'apple': 100,
    'banana': 200,
    'orange': 300,
}
print(fruits['apple'])

# 集合の使い所 ＊一例
# 共通点を出力
my_friends = {'A', 'C', 'D'}
A_friends = {'B', 'D', 'E', 'F'}
print(my_friends & A_friends)

# listのデータを型変換(cast)
f = ['apple', 'banana', 'apple', 'banana']
kind = set(f)
print(kind)