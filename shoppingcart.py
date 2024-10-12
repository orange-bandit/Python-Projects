
stock = {'pizza':15.00,
         'nachos': 12.50,
         'pop-corn':10.00,
         'potatoes': 20.00,
         'frost': 9.99,
         'ratbread': 4.99,
         'catbread': 6.99,
         'cornbread': 30.00,
         'bread': 60.00,
         'metalwater': 14.99}

cart = []

total = 0

print('----- MENU -----')
for key, value in stock.items():
    print(f'{key:10}: ${value:.2f}')



while True:
    print('----------------')
    print(f'-empty to empty cart,-cart to show cart contents,-quit to quit program,')
    choice = str(input(f'Enter your choice: ')).lower()

    if choice == ('quit' or '-quit'):
        print('----------------')
        print('goodbye')
        break
    elif choice == ('cart' or '-cart'):
        print('-- Your Cart ---')
        print(f'{cart}',end=' ')
        for item in cart:
            total += float(stock.get(item))
        print('----------------')
        total = round(total,3)
        print(f'your total is ${total:.2f}')
    elif choice == ('empty' or '-empty'):
        cart.clear()
        total = 0
        print('----------------')
        print('emptied cart')
    elif stock.get(choice) is not None:
        cart.append(choice)
        
        print(f'Added {choice} to your cart')
    elif stock.get(choice) is None:
        print(f'{choice} is not in stock')
