#1 create a function that picks a random item from the list
#2 create a function that checks if a number is even or odd
#3 create a function that prints the cube of a number
#4 create a function that checks if a letter is vowel or consonant

#1
import random
def pick_car():
   list_of_cars = ['toyota', 'bmw','benz','mazda']
   return random.choice(list_of_cars)
print(pick_car())

#2
def if_even(number):
   if number % 2 == 0:
      print('you entered an even number')
   else:
      print('you entered an odd number')

      
   return
if_even(8)

#3

#4
def vowel():
   vowel_letter = ['a','e','i','o','u']
   input_letter = input('enter any alphabet')
   if input_letter in vowel_letter:
    print('alphabet is a vowel')
   else:
      print('alphabet is a consonant')
   
   return 
   vowel(a)


