'''
modules are python files that contains python codes

'''
#built in modules e.g import math, random etc
import math
import add
import sub
from add import mul #selective import allows you to import a particular section of a file

print(math.sqrt(16))
print(add.add(5,17))
print(sub.sub(9,4))
print(mul(3,4))

#renaming module: math is renamed as perform_calculation
import math as perform_calculation   #renaming module
print(perform_calculation.sqrt(36))

#1 create a function that picks a random item from the list
#2 create a function that checks if a number is even or odd
#3 create a function that prints the cube of a number
#4 create a function that checks if a letter is vowel or consonant

import task
print(task.pick_car())

print(task.if_even(8))

from math_utils.basic_operation import *
from math_utils.advanced_operation import *

add(6,9)
sub(10,7)
div(10,5)
mul(4,2)



