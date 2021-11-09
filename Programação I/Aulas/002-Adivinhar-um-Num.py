import random

number = random.randint(1, 1000)
guesses = 0
while True:
    guess = int(input('Guess my number between 1 and 1000: '))
    guesses += 1

    if guess > number:
        print(f'{guess} is too high!')
    elif guess < number:
        print(f'{guess} is too low!')
    else:
        print('You got it right!\n')
        break

print(f'You only took {guesses} guesses!')
