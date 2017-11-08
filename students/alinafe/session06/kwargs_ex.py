#!/usr/bin/env python3

import kwargs_ex

def test_basic():
    assert True

def test_kw():
    result = kwargs_ex.fun(for_color="blue",
                           back_color="red",
                           link_color="yellow",
                           visited_color="green")

    assert result == ('blue','red','yellow', 'green')