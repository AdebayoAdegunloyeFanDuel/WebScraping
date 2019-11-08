from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import ssl

import re

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

site_links = []


def internal_link(linkURL):
    html = urlopen('https://treehouse-projects.github.io/horse-land/{}'
                   .format(linkURL))
    soup = BeautifulSoup(html, 'html.parser')

    return soup.find('a', href=re.compile('(.html)$'))


if __name__ == '__main__':
    urls = internal_link('index.html')
    while len(urls) > 0:
        page = urls.attrs['href']
        if page not in site_links:
            site_links.append(page)

            print(page)
            print('\n==================\n')
            urls = internal_link(page)

        else:
            break



