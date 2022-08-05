from test_package.tools import utils
# これは分かり難い為、推奨されていない
# from ..tools import utils

def sing():
    return '##fakfajdflja;dlfkjal;fkajf'

def cry():
    return utils.say_twice('fadfkaljsfad;slkfja;fkja')

if __name__ == '__main__':
    print(sing())
    print('animal:', __name__)