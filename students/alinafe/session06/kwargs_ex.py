#!/usr/bin/env python3

import kwargs_ex
import pytest

def fun(for_color='blue',
        back_color='red',
        link_color='yellow',
        visited_color='green'):

    return(for_color,back_color,link_color,visited_color)

def fun2(*args,**kwargs):
    return(args,kwargs)

def test_basic():
    assert True

def test_kw():
    result = kwargs_ex.fun(for_color='blue',
                           back_color='red',
                           link_color='yellow',
                           visited_color='green')

    assert result == ('blue','red','yellow', 'green')

def test_kw_new_order():
    result = kwargs_ex.fun(visited_color='green',
                           for_color='blue',
                           back_color='red',
                           link_color='yellow')

    assert result == ('blue','red','yellow', 'green')

def test_kw_new_order_pos():
    result = kwargs_ex.fun('blue',
                           'red',
                           'yellow',
                           'green',)

    assert result == ('blue','red','yellow', 'green')

def test_kw_new_combo():
    result = kwargs_ex.fun('blue',
                           'red',
                           visited_color='green',
                           link_color='yellow',
                          )

    assert result == ('blue','red','yellow', 'green')

def test_kw_new_combo_tup():
    tup = ('green',
            'blue',
            'purple',
            'yellow')
    result = kwargs_ex.fun(*tup)

   # assert result == ('green','blue','purple','yellow', )
    assert result == tup

def test_kw_dic():
    dic = {'for_color':'blue',
           'back_color':'red',
           'link_color':'yellow',
           'visited_color':'green'
           }
    result = kwargs_ex.fun(**dic)

    assert result == ('blue','red','yellow','green')
   # assert result == dic

def test_kw_combo_dic():
    tup = {'blue',
           'green'}

    dic = {#'for_color':'blue',
           #'back_color':'red',
           'link_color':'purple',
           'visited_color':'yellow'
           }
    result = kwargs_ex.fun(*tup,**dic)

    assert result == ('blue','green','purple','yellow')
   # assert result == dic


"""def test_kw_combo_bad():
    with pytest.raises(NameError):
        result = kwargs_ex.fun('red',
                               'blue',
                               visited_color='green',
                               link_color='yellow',
                               )
"""
def test_fun2():
    result = kwargs_ex.fun2()

    assert result == ((),{})

def test_fun3():
    result = kwargs_ex.fun2(2,3)

    assert result == ((2,3),{})

def test_fun3():
    result = kwargs_ex.fun2(this=45)

    assert result == ((),{'this':45})

def test_fun3_multi():
    result = kwargs_ex.fun2(4,5, this=45)

    assert result[0] == (4,5)
    assert result[1] == ({'this': 45})

def test_fun3_multi():
    t=(4,5,6,7)
    result = kwargs_ex.fun2(3,4,*t, this=45)

    assert result[0] == (3,4,4,5,6,7)
    assert result[1] == ({'this': 45})