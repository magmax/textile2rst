#!/usr/bin/env python

from __future__ import print_function

import re
import argparse
from collections import namedtuple


Link = namedtuple('Link',
                  ['original', 'link', 'text', 'alt'])


class Translator(object):
    def process(self, filename):
        return self.process_string(self._read_file(filename))

    def process_string(self, content):
        links = list(self._get_links(content))

        return self._replace(content, links) + self._printable_links(links)

    def _get_links(self, content):
        regex = '((?:"(.*?)":)?"(.*?)":(https?://.*?))\.?[,; \r\t$\n\(\)]'
        for m in re.finditer(regex, content, re.MULTILINE):
            yield Link(original=m.group(1), alt=m.group(2),
                       text=m.group(3), link=m.group(4))

    def _read_file(self, filename):
        with open(filename) as fd:
            return fd.read()

    def _printable_links(self, links):
        result = []
        for link in links:
            result.append(".. _`%s`: %s" % (link.text, link.link))
        return '\n'.join(result)

    def _replace(self, content, links):
        # replace links
        for link in links:
            content = content.replace(link.original, "`%s`_ " % link.text)

        # replace more
        content = re.sub('<!--\s*more\s*-->', '.. more', content)

        # replace hr
        content = re.sub('<hr\s*/?>', '----', content)

        # replace sections
        def section_repl(symbol):
            def inner(matchobj):
                return '%s\n%s' % (matchobj.group(1),
                                   len(matchobj.group(1)) * symbol)
            return inner
        for n, symbol in enumerate('=-~^_#%'):
            pat = '^h%d\.\s*(.*)$' % (n + 1)
            content = re.sub(pat, section_repl(symbol), content,
                             flags=re.MULTILINE)

        # replace code
        def code_repl(matchobj):
            lang = matchobj.group('lang')
            code = matchobj.group('code')
            return '.. code:: %s\n%s\n' % (
                lang,
                '\n'.join(('    ' + s if s.strip() else '')
                          for s in code.splitlines())
            )
        regex = (
            '\{%\s*highlight\s*(?P<lang>.*?)\s*%\}'
            '(?P<code>.*?)'
            '\{%\s*endhighlight\s*%\}'
        )
        content = re.sub(regex,
                         code_repl, content, flags=re.MULTILINE | re.DOTALL)

        return content


def main():
    parser = argparse.ArgumentParser(
        description='Translate old textile links into new style rst')
    parser.add_argument('filename', nargs=1,
                        help='File to be processed')

    args = parser.parse_args()

    translator = Translator()
    translator.process(args.filename[0])


if __name__ == '__main__':
    main()
