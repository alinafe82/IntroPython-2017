# Demo of a contextmanager


class Context(object):
    """
    from Doug Hellmann, PyMOTW
    https://pymotw.com/3/contextlib/#module-contextlib
    """

    def __init__(self, handle_error):
        print('__init__({})'.format(handle_error))
        self.handle_error = handle_error

    def __enter__(self):
        print('__enter__()')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('__exit__({}, {}, {})'.format(exc_type, exc_val, exc_tb))
        if exc_type == ValueError:
            return True
        else:
            return False
        #return self.handle_error

"""with Context(True) as cont:
    print("in the context")
    raise ValueError("An Error")
__init__(True)
__enter__()
in the context
('An Error',)
__exit__(<class 'ValueError'>, An Error, <traceback object at 0x104a88608>)
with Context(True) as cont:
    print("in the context")
    raise AttributeError("An Error")
__init__(True)
__enter__()
in the context
('An Error',)
__exit__(<class 'AttributeError'>, An Error, <traceback object at 0x104a88848>)
"""

