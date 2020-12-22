import unittest
from preprocessing.textExtractor import TextExtractor

class TestExtractingText(unittest.TestCase):

    def test_extracting_text(self):
        from bs4 import BeautifulSoup
        import requests
        url = 'https://medium.com/@ageitgey/machine-learning-is-fun-80ea3ec3c471'
        r = requests.get(url)
        html = r.text
        t = TextExtractor()

        text = t.extract_all_text(html)
        # soup = BeautifulSoup(html, 'lxml')
        #
        # links = soup.find_all('p', {'itemprop': 'articleBody'})
        print(text)
