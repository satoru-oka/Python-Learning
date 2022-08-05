import math

# math
result = math.sqrt(25)
print(result)

y = math.log2(10)
print(y)

# print(help(math))

# string
print('hello')
print("hello")
print("I don't know")
print('I don\'t know')
print('say "I don\'t know"')
print("say \"I don't know\"")

print('hello.\nHow are you?')
print(r'C:\name\name')

print('##################')
print("""\
line1
line2
line3\
""")
print('##################')

print('Hi.' * 3 + 'Mike.')

print('Py' + 'thon')
print('Py''thon')
prefix = 'Py'
print(prefix + 'thon')

s1 = ('aaaaaaaaaaaaaaaaa'
     'bbbbbbbbbbbbbbbbb')
print(s1)

s2 = 'aaaaaaaaaaaaaaaaa'\
     'bbbbbbbbbbbbbbbbb'
print(s2)

# string index slice
word = 'python'
print(word[0])
print(word[1])
print(word[5])
print(word[-1])
print(word[0:2])
print(word[2:5])
print(word[0:2])
print(word[:2])
print(word[2:])

print(word[:])
word = 'j' + word[1:]
print(word[:])
print(len(word))

# string method
s = 'My name is Mike. Hi Mike.'
print(s)
is_start = s.startswith('My')
print(is_start)
is_start = s.startswith('X')
print(is_start)

print("###################")

print(s.find('Mike'))
print(s.rfind('Mike'))
print(s.count('Mike'))
print(s.capitalize())
print(s.title())
print(s.upper())
print(s.lower())
print(s.replace('Mike', 'Nancy'))

# string assignment
# f-string python3.6~
a = 'a'
print(f'a is {a}')

x, y, z = 1, 2, 3
print(f'a is {x}, {y}, {z}')
print(f'a is {z}, {y}, {x}')

name = 'Jun'
family = 'Sakai'
print(f'My name is {name} {family}. I am a {family} {name}')