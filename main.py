from laptops import *
from computers import *
from monitors import *
from tablets import *
from cables_and_adapters import *
from microphones import *
from software import *

def main():
    print(Fore.LIGHTWHITE_EX + '''[laptops] = laptops
[computers] = computers
[monitors] = monitors
[tablets] = tablets
[cables_and_adapters] = cables and adapters
[microphones] = microphones
[software] = software''')

    goods = input(': ')

    if goods == 'laptops':
        brand = input('Enter the brand: ')
        laptops(brand)

    elif goods == 'computers':
        brand = input('Enter the brand: ')
        computers(brand)

    elif goods == 'monitors':
        brand = input('Enter the brand: ')
        monitors(brand)

    elif goods == 'tablets':
        brand = input('Enter the brand: ')
        tablets(brand)

    elif goods == 'cables_and_adapters':
        cables_and_adapters()

    elif goods == 'microphones':
        brand = input('Enter the brand: ')
        microphones(brand)

    elif goods == 'software':
        software()

while True:
    main()