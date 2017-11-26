class Element:
    tag = 'html'
    indent = '  '

    # where content is expected to be a string – and defaults to Nothing.
    def __init__(self, content=None):
        if content is None:
            self.content = []
        else:
            self.content = [content]

    # It should have an append method that can add another string to the content.
    def append(self, content):
        self.content.append(content)

    # Should be a list
    def render(self, file_obj):
        all_content = ('<' + self.tag + '>')
        for each in self.content:
            try:
                all_content += each
            except TypeError:
                each.render(file_obj)
        all_content += '</' + self.tag + '>'

        self.write_to_file(file_obj, all_content)

    def write_to_file(self, file_obj, stuff_to_print):
        file_obj.write(stuff_to_print)


class Body(Element):
    tag = 'body'


class Para(Element):
    tag = 'p'


class HTML(Element):
    tag = 'html'