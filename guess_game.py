import random
target_number = random.randint(1,10)
guess = None
while guess != target_number:
    guess = int(input('enter any random number from 1 t0 30 = '))
    if guess < target_number:
        print('choose a bigger number')
    elif guess > target_number:
        print('choose a lesser number')
   
    else:
        print(f'hurray, the number guessed is {target_number}')