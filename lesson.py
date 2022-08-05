# builtins function
import builtins
from termcolor import colored
from test_package.talk import animal
import test_package.talk.animal

builtins.globals()
print(globals())

ranking = {
    'A': 100,
    'B': 85,
    'C': 95
}

for key in ranking:
    print(key)

print(sorted(ranking, key=ranking.get, reverse=True))

# python library
# Library not used
s = 'faldsakfjadslfkjadsfjas;lkfdja;sdlfkjasd;ldfjka;lsf'

d = {}
for c in s:
    if c not in d:
        d[c] = 0
    d[c] += 1
print(d)

d = {}
for c in s:
    d.setdefault(c, 0)
    d[c] += 1
print(d)

from collections import defaultdict


d = defaultdict(int)
for c in s:
    d[c] += 1
print(d)

print(d['f'])

print(colored('test', 'green'))
# print(help(colored))

def main():
    test_package.talk.animal.sing()

if __name__ == '__main__':
    main()