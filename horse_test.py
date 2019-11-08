from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import ssl

import unittest

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context


class TestHorseLand(unittest.TestCase):
    soup = None

    def setUpClass():
        url = 'https://treehouse-projects.github.io/horse-land/index.html'

        TestHorseLand.soup = BeautifulSoup(urlopen(url), 'html.parser')

    def test_header1(self):
        header1 = TestHorseLand.soup.find('h1').get_text()
        self.assertEqual('Horse Land', header1)


if __name__ == '__main__':
    unittest.main()