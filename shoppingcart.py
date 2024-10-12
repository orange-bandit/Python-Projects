stock = {
    'pizza': 15.00, 'nachos': 12.50, 'pop-corn': 10.00,
    'potatoes': 20.00, 'frost': 9.99, 'ratbread': 4.99,
    'catbread': 6.99, 'cornbread': 30.00, 'bread': 60.00,
    'metalwater': 14.99
}

cart = []
total = 0

def display_menu():
    print('----- MENU -----')
    for item, price in stock.items():
        print(f'{item:10}: ${price:.2f}')

def display_cart():
    print('-- Your Cart ---')
    print(', '.join(cart) if cart else "Empty")
    print('----------------')
    print(f'Your total is ${total:.2f}')

def add_to_cart(item):
    global total
    if item in stock:
        cart.append(item)
        total += stock[item]
        print(f'Added {item} to your cart')
    else:
        print(f'{item} is not in stock')

def empty_cart():
    global total
    cart.clear()
    total = 0
    print('Emptied cart')

def main():
    display_menu()
    
    while True:
        print('----------------')
        print('-empty to empty cart, -cart to show cart contents, -quit to quit program')
        choice = input('Enter your choice: ').lower().strip()

        if choice in ('quit', '-quit'):
            print('----------------')
            print('Goodbye')
            break
        elif choice in ('cart', '-cart'):
            display_cart()
        elif choice in ('empty', '-empty'):
            empty_cart()
        else:
            add_to_cart(choice)

if __name__ == "__main__":
    main()