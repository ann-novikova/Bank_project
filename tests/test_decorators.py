import pytest
from src.decorators import log

def test_log_no_filename(capsys):
    @log(filename=None)
    def my_function(x, y):
        return x + y

    my_function(1, 2)
    captured = capsys.readouterr()
    assert captured.out == 'my_function ok\n'

    my_function('line', 3)
    captured = capsys.readouterr()
    assert captured.out == "my_function error: can only concatenate str (not \"int\") to str. Inputs: ('line', 3), {}\n"

def test_log_with_filename():
    @log(filename='mylog.txt')
    def my_function(x, y):
        return x + y

    my_function(10, 20)
    with open('mylog.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    assert lines[-1].strip() == 'my_function ok'

    my_function((10, 100, 5), 20)
    with open('mylog.txt', 'r', encoding='utf-8') as file:
        lines = file.readlines()
    assert lines[-1].strip() == 'my_function error: can only concatenate tuple (not "int") to tuple. Inputs: ((10, 100, 5), 20), {}'

