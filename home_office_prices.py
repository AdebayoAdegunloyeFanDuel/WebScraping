import requests
from bs4 import BeautifulSoup

my_budget = int(input("What is your budget? Enter a whole number: "))


def find_home_desk():
    read = requests.get('https://www.johnlewis.com/browse/furniture-lights/home-office/office-desks/_/N-c6c')
    content = read.content
    soup = BeautifulSoup(content)
    element = soup.find('span', {'class': 'product-card__price-span',
                                 'data-test': 'product-card__price product-card__price--current'})

    price = element.text.strip()
    price_no_currency = price[1:]
    price_number = float(price_no_currency)
    print(price_number)

    if price_number > my_budget:
        print("This item is over my budget... Sorry next time!")
    else:
        print("Lets buy it!")


find_home_desk()





