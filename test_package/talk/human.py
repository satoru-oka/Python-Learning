from test_package.tools import utils
# これは分かり難い為、推奨されていない
# from ..tools import utils

def sing():
    return 'sing'

def cry():
    return utils.say_twice('cry')