#weight calculator

weight = float(input('enter your weight: '))
unit = input('is that in kilograms or pounds? (K or L): ')



if unit == 'K':
    weight = weight * 2.205
    unit = 'Lbs.'
    print(f'Your weight is: {round(weight,2)} {unit}')
elif unit == 'L':
    weight = weight/2.205
    unit = 'Kgs.'
    print(f'Your weight is: {round(weight,2)} {unit}')
else:
    print(f'{unit} was not valid')
