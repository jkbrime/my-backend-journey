'''
function in python it is a block of organised reusable code
'''
#def name_of_function(parameters):
    #block of code
    #return value

import random

def greet(name):
    message = f'hello {name}'
    return message
print(greet('jide'))

def smile(name):
    message = f'hello {name}'
    return message
print(smile('Olajide'))

def add(a,b):
    sum = a + b
    return sum
print(add(8,9))

# 1. write a function that checks if a number is even number
# 2. write a function that sums all the numbers in a list
# 3. write a function that gets the maximum number in a list
# 4. calculate the area of a circle
# 5. write a function that finds the common difference between two lists
# 6. write a function that performs a rolling dice number

#1
def if_even(number):
   if number % 2 == 0:
      print('you entered an even number')
   else:
      print('you entered an odd number')
      
   return
if_even(9)

#2
def total(list_of_numbers):
    return sum(list_of_numbers), max(list_of_numbers)
print(total([1,2,3,4,5]))

#3 max(list_of_numbers) as shown above

#4
def area_of_a_circle(radius):
    pi= 3.142
    return pi*radius**2
print(area_of_a_circle(7))

#5
def common_diff(list1,list2):
    return list(set(list1) & set(list2))
print(common_diff([1,4,5,6], [3,4,7,8]))

#6
def dice_roll():
 return random.randint(1,6)
print(dice_roll())

def looper():
   list_of_item = ['iphone11', '£20','1harmstar','£1000000']
   return random.choice(list_of_item)
print(looper())

'''
def shop():
   cash_at_hand = 100
   item_price = int(input('price of item'))
   if cash_at_hand >= item_price:
      balance = cash_at_hand - item_price
      print(f'transaction gone and your balance {balance}')
   else:
      print('fund your wallet')
      return
   
shop()
'''

user = {}
def registration_of_user():
  user ['username'] = input('your user name  ')
  user ['password'] = input('password  ')
  if user['username'] in user:
      print('username exist')
      user['username'] = input('enter a valid username')
  else:
     print('registration done')

registration_of_user()
   

