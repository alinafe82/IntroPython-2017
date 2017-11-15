from html_render import Element


def test_new_element():
    el_object = Element('content')  # capital E as it is a class
    el_object2 = Element()  # capital E as it is a class


# test functionality
def test_add_element():
    el_object = Element('content')  # capital E as it is a class
    print(el_object.content)
    el_object = Element()
    assert el_object.content == []
    # assert False


def test_adding_empty_string():
    el_object = Element('')
    assert el_object.content == ['']


def test_append_string():
    el_object = Element('spam, spam, spam')
    el_object.append(', wonderful spam')
    assert el_object.content == ['spam, spam, spam', ', wonderful spam']


def test_tag_element():
    assert Element.tag == 'html'
    el_object = Element('spam, spam, spam')
    assert el_object.tag == 'html'


def test_indent_exists():
    assert Element.indent == '  '


def test_render():
    my_stuff = 'spam, spam, spam'
    el_object = Element('spam, spam, spam')
    with open('test1', 'w') as out_file:
        el_object.render(out_file)
    with open('test1', 'r') as in_file:
        contents = in_file.read()
    assert contents.startswith('<html>')
    assert contents.endswith('</html>')
    assert my_stuff in contents