'''
data structure

'''
my_list = ['temi', 'saviour', 'sekinat', 'gozie', 'jide', 'timi', 1,2,3,4,26,True,False]

my_list2 = list(range(10))

print(my_list)
print(my_list2)

timi_name = my_list[5]

print('hello ' + timi_name)

print(f'hello {my_list[4]} and i am {my_list[10]}') # the f string is to be able to print strings and integers
print(my_list2[-1])

print(my_list[2:5]) #slicing is to list a range of data, eg sekinat to jide

my_list[6] = 'joy' #to add joy to the list of names on the data
print(my_list)

my_list.append(1) #it adds a data to the end of existing data
print(my_list)

my_list.insert(7, 'joel') #to insert a name in a particuler place
print(my_list)

my_list.pop(-1) #to remove from the end
print(my_list)

my_list.pop(4)
print(my_list)

my_list.insert(4, 'jide')
print(my_list)

my_list.remove(4)
print(my_list)

my_list.append('jide')
print(my_list)

my_list.count('jide')
print(my_list.count('jide'))

print(my_list.clear()) # to clear
print(my_list)

list_of_fruits = ['orange', 'mango', 'banana', 'apple', 'guava','berry', 'pineapple']
print('my favourite fruit is ' + list_of_fruits[2])
list_of_fruits.append('grape')
print(list_of_fruits)

print(list_of_fruits[2:5])

list_of_fruits.remove('grape')
print(list_of_fruits)

'''turple'''#a data that cant be altered or changed
my_turple = () #empty turple
single_turple = ('jide',) #single turple
multiple_turple = ('jkbrime', 'olalekan', 'banana', ['lagos', 'osun', 'oyo', 'kano'], 1,3,4,True,False)
my_turple2 = ('[1,3,4,5,6,7]')
print(multiple_turple[3])
print(multiple_turple[2:6])
print(len(multiple_turple))
turple1 = (1,2,3)
turple2 = (4,5,6)
con_turple = turple1 + turple2
print(con_turple)
turple1 = (1,2,3,4)
turple2 = (5,6,7,8)
turple3 = (9,10,11,12)
con_turple = turple1 + turple2 + turple3
print(con_turple)

my_foods = ('rice', 'beans', 'eggs') #converting from tuple data type to list data type
my_foods_list = list(my_foods)
print(my_foods_list)
tuple_food = tuple(my_foods_list)
print(tuple_food)
print(tuple_food * 3)
'''NOTE:tuple has normal bracket while list has block bracket'''
