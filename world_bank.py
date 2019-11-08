from urllib.request import urlopen
from bs4 import BeautifulSoup
import csv


# Get Country
def get_country(country_code):
    html = urlopen('http://api.worldbank.org/v2/country/{}'
                   .format(country_code))

    #Soup object
    soup = BeautifulSoup(html, 'xml')

    country_name = soup.find('wb:name')
    region = soup.find('wb:region')
    income_level = soup.find('wb:incomeLevel')

    print(country_name.get_text())
    print(region.get_text())
    print(income_level.get_text())


#read the iso csv file and looping through the ISO code; meaning country code


if __name__=='__main__':
    with open('country_iso_codes.csv', 'r') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for code in csv_file:
            writer.writerow(code)
            get_country(code[0])

