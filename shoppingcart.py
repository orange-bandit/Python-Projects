
foods = []
prices = []
total = 0

while True:
    food = input('Enter you preferred food purchase: (Q to Quit)')
    if food == 'Q' or food == 'q':
        break
    else:
        price = int(input(f'Enter the price for {food}: $'))
        foods.append(food)
        prices.append(price)


print('----- Your Cart -----')

for food in foods:
    print(food)

for price in prices:
    total += price

print(f'Your total is: ${total}')