#quiz game demo
import time


questions = (
    'How many elements are in the periodic table?: ',
    'WHich animal lays the largest eggs?: ',
    'what is the most abundant gas in Earths atmosphere?: ',
    'How many bones are in the human body?: ',
    'WHich planet in the milkyway is the hottest?:'
)
options = (('A. 116','B. 117','C. 118','D. 119'),
           ('A. Whale','B. Crocodile','C. ELephant','D. Ostrich'),
           ('A. Nitrogen','B. Oxygen','C. Carbon-Dioxide','D. Hydrogen'),
           ('A. 206','B. 207','C. 406','D. 407'),
           ('A. Mecury','B. Venus','C. Earth','D. Mars'))

answers = ('C','D','A','A','A')
guesses = []
score = 0

question_num = 1

for question in questions:
    print('----------------')
    print(f'{question_num}')
    print(question)

    for option in options[question_num-1]:
        print(option)

    guess = input('Enter (A,B,C,D): ').upper()
    guesses.append(guess)

    if guess == answers[question_num-1]:
        score += 1
        print('You Guessed CORRECT!!')
    else:
        print('You Guessed INCORRECT!!')
        print(f'{answers[question_num-1]} is the correct answer!' )
    
    time.sleep(1)

    question_num+=1


print('--------------------')
print('-    RESULTS       -')
print('--------------------')

print(f'Your Score is: {score}')

print('answers: ',end='')
for answer in answers:
    print(f'{answer}-',end='')
print()

print('guesses: ',end='')
for guess in guesses:
    print(f'{guess}-',end='')
print()

print(f'THANKS FOR PLAYING')