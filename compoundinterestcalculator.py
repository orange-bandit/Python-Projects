#compound interest calculator in python

principle= 0
rate = 0
time = 0

while True:
    principle = float(input('enter principle amount: '))
    if principle < 0:
        print('principle cant be less or equal to zero')
    else:
        break

while True:
    rate = float(input('enter the interest rate: '))
    if rate < 0:
        print('interest rate cant be less or equal to zero')
    else:
        break


while True:
    time = int(input('enter time in years: '))
    if time < 0:
        print('time cant be less or equal to zero')
    else:
        break

total = principle * pow((1 + rate / 100),time)

print(f'Balance after {time} year/s: ${total:.2f}')