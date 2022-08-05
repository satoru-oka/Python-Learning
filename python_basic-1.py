# Variable Declaration 1
num = 1
name = 'Mike'
is_ok = True

# Variable Declaration 2
num2: int = 2
name2: str = 'Mark'
is_ok2: bool = False

# type() data type confirmation
# 1
print(num, type(num))
print(name, type(name))
print(is_ok, type(is_ok))

# 2
print(num2, type(num2))
print(name2, type(name2))
print(is_ok2, type(is_ok2))

# print() セパレーションの記述と改行も指定
# 改行は end='\n' 記述指定しなくても改行される挙動
print('Hi', 'Mike')
print('Hi', 'Mike')
print('Hi', 'Mike', sep=',', end='\n')
print('hi', 'mike', sep=',', end='\n')