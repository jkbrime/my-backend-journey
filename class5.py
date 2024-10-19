'''
loops are used to repeat a block of codes multiple times

'''
names = ['bola', 'tunde', 'ceejay']
for name in names:
    print(f'hello {name}')
strings = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
for letter in strings:
    print(letter)

for O in range(5):
    print('I LOVE YOU')

for i in range(10):
    print('I LOVE PYTHON')

person = {'name' : 'jide', 'age' : 60,'state' : 'osun'}
for key, value in person.items():
    print(f'{key} is {value}')

for number in range(1,20):
    if number % 2 == 0:
        print(number)

'''
Tested loop is a loop inside another loop
'''
classes = ['class_1', 'class_2', 'class_3']
students = ['student1', 'student2', 'student3', 'student4','student5']
for clas in classes:
    for rep in students:
        print(clas, rep)

Alph = ['A', 'B', 'C']
B = [f'a1', 'b2', 'c3']
for alp in Alph:
    for rep in B:
        print(alp, rep)

for letter in ['A','B','C']:
    for number in [1,2,3,4]:
        print(letter, number)

for number1 in [2]:
 for number2 in [1,2,3,4,5,6]:
  product = number1 * number2
  print(product)

for number in range(1,6):
    for num in range(1,6):
       
        product = number * num
        print(f'{number} * {num} = {product}')

records = [
    {'user_name': 'jide', 'password': 1441},
    {'user_name': 'timi', 'password': 2334},
    {'user_name': 'gozie', 'password': 5442},
]
for record in records:
    for key, value in record.items():
        print(f'{key} = {value}')

for number in range(1,5):
    if number >= 5:
        break
    print(number)

count = 0
while count < 10:
    print('i love you')
    count +=1

count = 0
while count < 10:
    print(count)
    count +=1
    