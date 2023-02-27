from datetime import date
from products import products
import sys


def add_shooping_cart():
    shop_price = 0
    shop_list = []
    user_choice = input('KOD KRESKOWY LUB WYDRUK PARAGONU(P) :')
    while user_choice != 'P':
        shop_list.append(products[user_choice]['name'])
        shop_list.append(products[user_choice]['price'])
        shop_price += products[user_choice]['price']
        user_choice = input('KOD KRESKOWY LUB WYDRUK PARAGONU(P) :')
    return shop_list, shop_price


def game():
    print('WYBIERZ OPCJĘ:')
    print('1 => LISTA WSZYSTKICH PRODUKTÓW')
    print('2 => ZAKUPY')
    print('3 => ZAKOŃCZ PROGRAM')
    user_choice = input('WYBIERZ 1, 2 LUB 3:')
    if user_choice == '1':
        product_list()
    elif user_choice == '2':
        carts = add_shooping_cart()
        print('---------------------------------')
        print('PARAGON')
        print(date.today())
        print('---------------------------------')
        products_list = list(carts[0])
        i = 0
        for i in range(len(products_list)):
            if i % 2 == 1:
                print(f'{products_list[i-1]} | {products_list[i]} zł')

        print('---------------------------------')
        print(f'DO ZAPŁATY: {round(carts[1],2)} zł')
        print(f'W TYM VAT: {round(carts[1]*0.23,2)} zł')
    elif user_choice == '3':
        sys.exit(0)


def product_list():
    print('KOD KRESKOWY | NAZWA')
    for product, product_info in products.items():
        print(f'{product} | {product_info["name"]}')
    game()


if __name__ == "__main__":
    game()

