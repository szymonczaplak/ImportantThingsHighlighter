import re

from bs4 import BeautifulSoup

class TextExtractor:
    def __init__(self):
        self.blacklist = [
            '[document]',
            'noscript',
            'header',
            'html',
            'meta',
            'head',
            'input',
            'script'
        ]


    def extract_all_text(self, htmlContent):
        soup = BeautifulSoup(htmlContent, 'html.parser')
        texts = [e.get_text() for e in soup.find_all('article') if e.parent.name not in self.blacklist]
        output = ''
        for t in texts:
            output += '{}. '.format(t)
        return re.sub(' +', ' ', output)
