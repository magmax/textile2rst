import unittest

from textile2rst.textile2rst import Translator


class TestTranslator(unittest.TestCase):
    def setUp(self):
        self.sut = Translator()

    def test_simple_string(self):
        assert 'foo bar' == self.sut.process_string('foo bar')

    def test_replace_more(self):
        assert 'foo\n.. more\nbar' == self.sut.process_string('foo\n<!-- more  -->\nbar')

    def test_replace_hr_in_html(self):
        assert 'foo\n----\nbar' == self.sut.process_string('foo\n<hr/>\nbar')
        assert 'foo\n----\nbar' == self.sut.process_string('foo\n<hr />\nbar')

    def test_replace_sections(self):
        assert 'title\n=====' == self.sut.process_string('h1. title')
        assert 'title\n-----' == self.sut.process_string('h2. title')
        assert 'title\n~~~~~' == self.sut.process_string('h3. title')
        assert 'title\n^^^^^' == self.sut.process_string('h4. title')
        assert 'title\n_____' == self.sut.process_string('h5. title')
        assert 'title\n#####' == self.sut.process_string('h6. title')
        assert 'title\n%%%%%' == self.sut.process_string('h7. title')

    def test_replace_code(self):
        code = """
             {% highlight python %}
             def foo(self): pass
             {% endhighlight %}
        """
        expected = """
             .. code:: python

                 def foo(self): pass


        """
        assert expected == self.sut.process_string(code)

    def test_replace_link(self):
        text = '"message":http://web.page\n'
        expected = '`message`_ \n.. _`message`: http://web.page'

        assert expected == self.sut.process_string(text)

    def test_replace_links(self):
        text = '"message 1":http://web.page1\n"message 2":http://web.page2\n'
        expected = '`message 1`_ \n`message 2`_ \n.. _`message 1`: http://web.page1\n.. _`message 2`: http://web.page2'

        assert expected == self.sut.process_string(text)
