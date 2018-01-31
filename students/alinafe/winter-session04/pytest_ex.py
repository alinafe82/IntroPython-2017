# content of test_sample.py
import pytest


def inc(x):
    return x + 1


def test_answer():
    assert inc(3) == 5


def f():
    raise SystemExit(1)


def test_mytest():
    with pytest.raises(SystemExit):
        f()

class TestClass(object):
    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, 'check')


def test_needsfiles(tmpdir):
    print (tmpdir)
    assert 0