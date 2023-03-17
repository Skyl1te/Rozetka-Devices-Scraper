from libraries import *


def cables_and_adapters():
    # URL of the page to scrape
    url = 'https://rozetka.com.ua/tv-cables/c80073/'

    # Send a GET request to the URL
    response = requests.get(url)

    # Create a BeautifulSoup object and pass in the HTML parser
    soup = BeautifulSoup(response.content, 'html.parser')

    # Find all products on the page
    products = soup.find_all('div', {'class': 'goods-tile__inner'})

    # Loop through each product and extract information about its price, name, and rating
    for product in products:
        name = Fore.RED + str(product.find('span', {'class': 'goods-tile__title'}).text)

        old_price = Fore.YELLOW + '\u0336'.join(
            str(product.find('div', {'class': 'goods-tile__price--old price--gray ng-star-inserted'}).text)) \
                    + '\u0336' if product.find('div', {
            'class': 'goods-tile__price--old price--gray ng-star-inserted'}) else Fore.YELLOW + 'None'

        price = Fore.LIGHTGREEN_EX + str(product.find('span', {'class': 'goods-tile__price-value'}).text)

        feedbacks_element = product.find('span', {'class': 'goods-tile__reviews-link'})
        feedbacks = Fore.LIGHTCYAN_EX + str(feedbacks_element.text) if feedbacks_element else Fore.LIGHTCYAN_EX + 'None'

        sale_element = product.find('span',
                                    {'class': 'goods-tile__label promo-label promo-label_type_action ng-star-inserted'})
        sale = Fore.LIGHTMAGENTA_EX + 'Yes' if sale_element else Fore.LIGHTMAGENTA_EX + 'None'

        free_shipping_element = product.find('img', {'class': 'ng-failed-lazyloaded ng-lazyloaded ng-star-inserted'})
        free_shipping = Fore.LIGHTBLUE_EX + 'Yes' if free_shipping_element else Fore.LIGHTBLUE_EX + 'None'

        # Print the extracted information
        print(f'''{name}: 
              {Fore.MAGENTA}Old price: {old_price}
              {Fore.MAGENTA}New price: {price}
              {Fore.MAGENTA}Feedbacks: {feedbacks}
              {Fore.MAGENTA}Sale: {sale}
              {Fore.MAGENTA}Free shipping: {free_shipping}
{Fore.LIGHTBLACK_EX}___________________________________________________________________________
        ''')
