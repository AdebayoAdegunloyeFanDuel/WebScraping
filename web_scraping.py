from urllib.request import urlopen
from bs4 import BeautifulSoup
import os
import ssl

if (not os.environ.get('PYTHONHTTPSVERIFY', '') and
    getattr(ssl, '_create_unverified_context', None)):
    ssl._create_default_https_context = ssl._create_unverified_context

html = urlopen('https://treehouse-projects.github.io/horse-land/index.html')
soup = BeautifulSoup(html.read(), 'html.parser')


# divs = soup.find('div', {'class': 'featured'})
# print(soup.div)


# featured_header = soup.find('div', {'class': 'featured'})
# print(featured_header.get_text())

# for button in soup.find(class_='button button--primary'):
#     print(button)


for link in soup.find_all('a'):
    print(link.get('href'))