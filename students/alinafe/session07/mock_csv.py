
import unittest.mock as mock
import csv


def please_work(input_file):
    rate_all = csv.reader(open(input_file))
    #return ''.join([''.join(x) for x in rate_all])
    return [x for x in rate_all]


def test_thing():
    with mock.patch('builtins.open', return_value='brian') as m:
        result = please_work('foo')

    m.assert_called_once('foo')
    assert result == 'brian'


    """for x in rate_all:
        print(x)"""