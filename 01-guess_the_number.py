import random
answer = random.randint(1, 99)

name = input('What is your name? ')
guess = int(input('What is your guess? '))
# guess = int(guess)

while guess != answer:
    
    if guess > answer:
        print('Mine is smaller!')
    else:
        print('Mine is bigger!')
    
    guess = int(input('What is your guess? '))
    
    
print('WWWWOOOOWWW!!', name, 'You DID IT!!')  