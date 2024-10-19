'''operators'''
a = 5
b = 5
d = a + b
print(f'the addition of a and b is {d}')
d = b - a
print(f'the substration of b and a is {d}')
d = a * b
print(f'the multiplication of a and b is {d}')
d = a / b
print(f'the division of b and a is {d}')
d = b / a
print(f'the division of a and b is {d}')
d = b // a
print(f'the round up of a and b is {d} ')
d = a % b
print(f'the remainder of a and b is {d}')

'''comparism operator'''
#equal
y = a==b
print(f'a and b are equal...{y}')
g = a > b
print(f'is a greater than b...{g}')
g = a < b
print(f'is a lesser than b...{g}')
u = a !=b #not equal
print(f'a and b are not equal...{u}')
o = a < b
print(f'a is lesser than b...{o}')
i = a >= b
print(f'a is greater than equal to...{i}')
j = a <= b
print(f'a is lesser than equal to b...{j}')

'''logical operator'''
#and
print(a and b)

y = 6 + 7
z = 9 + 6
print(y and z)
print(y or z)
print(z or y)
y = 6 == 6
z = 6 == 6
print(z and y)
print(z or y)
print(not y)

#assignment operator
g = 2
g+=8
print(g)
g*=8
print(g)
g-=5
print(g)
g/=5
print(g)

'''conditional statements''' #sintax for conditional statement is if condition: code

'''
if condition:
   code
'''
x = 7
if x < 6:
    print('x is greater than 6')
else:
    print('na lie')

    '''write a python program to check if an accountant balance is sufficient for withdrawal'''

'''
deposit = int(input('boss deposit your money'))
get_cash = int(input('get cash'))
if deposit >= get_cash:
 print('take your money')

else:
 print('guy you are broke')
balance = deposit - get_cash
print(f'your balance is now {balance}')

username = input(f'enter your username')
password1 = input(f'enter your password')
password2 = input(f're enter your password')

if password1 == password2:
   print('signed up successful')

else:
   print('incorrect password')

'''
'''
user_bio_data = {}
user_bio_data['username'] = input('enter your username')
user_bio_data['sex'] = input('enter your sex')
user_bio_data['state'] = input('enter your state')
user_bio_data['age'] = input('enter your age')
user_bio_data['phone number'] = input('enter your phone number')
user_bio_data['password1'] = input('enter password')
user_bio_data['password2'] = input('re enter password')
print(user_bio_data)
if user_bio_data['password1'] == user_bio_data['password2']:
   print('your biodata has been collected')
else:
   print('correct your password')

assignment

   1. write a python program to check if a number is even or odd, if it is even print even and if it is odd, print odd
   2. write a python code to check a student grade based on their score
   3. write a python program to check if a number is positive, negative or zero
   4. write a python program to check if a year is a leap year
   all variables must be gotten from an input user
   '''
#1
num = int(input('enter any number to check whether it is odd or even'))
if (num % 2) == 0:
    print('The number is even')
else: print('The number is odd')

#2
enter_marks = int(input('enter the marks (0 - 100)'))
if 0 <= enter_marks <= 100:
    if enter_marks >= 90: grade = 'A'
    elif enter_marks >= 80: grade = 'B'
    elif enter_marks >= 70: grade = 'C'
    elif enter_marks >= 60: grade = 'D'
    else: grade = 'F'
    print('grade:', grade)
    #else:
    print('invalid marks. Please enter a value between 0 and 100')

#3
num = int(input('input a number '))
if num > 0:
    print('it is a positive number')
elif num == 0:
    print('it is zero')
else:
    print('it is negative')

#4
'''
year = int(input('input a year'))
if (year % 4 == 0 and (year % 100 ! = 0 or year % 400 == 0)):
    print(f'{year} is a leap year')
else:
    print(f'{year} is not a leap year')
'''






