class Element:
    tag = 'html'
    indent = '    '

    # where content is expected to be a string – and defaults to Nothing.
    def __init__(self, content=None):
        # import pdb; pdb.set_trace()
        if content is None:
            self.content = []
        else:
            self.content = [content]

 """def __init__(self, tag, attrib={}, **extra):
        if not isinstance(attrib, dict):
            raise TypeError("attrib must be dict, not %s" % (
                attrib.__class__.__name__,))
        attrib = attrib.copy()
        attrib.update(extra)
        self.tag = tag
        self.attrib = attrib
        self._children = []

        def __repr__(self):
        return "<%s %r at %#x>" % (self.__class__.__name__, self.tag, id(self))


        def makeelement(self, tag, attrib):
        Create a new element with the same type.
        *tag* is a string containing the element name.
        *attrib* is a dictionary containing the element attributes.
        Do not call this method, use the SubElement factory function instead.
        
        return self.__class__(tag, attrib)

    def copy(self):
        Return copy of current element.
        This creates a shallow copy. Subelements will be shared with the
        original tree.
        
        elem = self.makeelement(self.tag, self.attrib)
        elem.text = self.text
        elem.tail = self.tail
        elem[:] = self
        return elem

    def __len__(self):
        return len(self._children)

    def __bool__(self):
        warnings.warn(
            "The behavior of this method will change in future versions.  "
            "Use specific 'len(elem)' or 'elem is not None' test instead.",
            FutureWarning, stacklevel=2
            )
        return len(self._children) != 0 # emulate old behaviour, for now

    def __getitem__(self, index):
        return self._children[index]

    def __setitem__(self, index, element):
        # if isinstance(index, slice):
        #     for elt in element:
        #         assert iselement(elt)
        # else:
        #     assert iselement(element)
        self._children[index] = element

    def __delitem__(self, index):
        del self._children[index]

     def append(self, subelement):
        --Add *subelement* to the end of this element.
        --The new element will appear in document order after the last existing
        --subelement (or directly after the text, if it's the first subelement),
        --but before the end tag for this element.

        self._assert_is_element(subelement)
        self._children.append(subelement)

    def extend(self, elements):
        --Append subelements from a sequence.
        --*elements* is a sequence with zero or more elements.

        for element in elements:
            self._assert_is_element(element)
        self._children.extend(elements)

        """


    # It should have an append method that can add another string to the content.
    def append(self, content):
        self.content.append(content)
        #self.__children.append(content)

    # Should be a list
    def render(self, out_file, ind=""):
        if self.tag == 'html':
            out_file.write('<!DOCTYPE html>')
        out_file.write('\n')
        out_file.write(ind + '<' + self.tag + '>')
        for each in self.content:
            try:
                each.render(out_file, ind + self.indent)
            except AttributeError:
                out_file.write('\n' + ind + self.indent + str(each))
        if ind != "":
            out_file.write('\n' + ind)
        out_file.write('</' + self.tag + '>')

    def write_to_file(self, file_obj, stuff_to_print):
        file_obj.write(stuff_to_print)

class Body(Element):
    tag = 'body'


class Para(Element):
    tag = 'p'


class HTML(Element):
    tag = 'html'


class Head(Element):
    tag = 'head'


class OneLineTag(Element):

    def render(self, out_file, ind=""):
        out_file.write('\n' + ind + '<' + self.tag + '>')
        for each in self.content:
            try:
                each.render(out_file)
            except AttributeError:
                out_file.write(str(each))
        out_file.write('</' + self.tag + '>')

"""
e = the_function('stock'. s)
e
<Element 'Stock' at 0xx...>
e.set('_id','1234')

def dict_to_html_str(tag, d)

    parts = ['<{}>.format(tag)]
    for key, val in d.items():
        parts.append('<{0}>{1}</{0}>'format(key, val))
    parts.append('</{}>'format(tag))
    return ''.join(parts)

    d = {'name' " '<spam>'}
    dict_to_html_str('item', d)
    """