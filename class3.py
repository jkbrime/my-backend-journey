'''
set is an unordered collection of unique immutable (unchangeable) element and they are defined using {}
'''

set1 = {1,2,3,4,5,4,'apple'}
print(set1)
name_of_set1 = {7,6,8,5,4,8,9}
print(set1)
empty_set = set()
'''create a list'''
my_list = [1,2,3,4,5,3,4,5,3,6,7,"apple"]
con_list = set(my_list)
print(con_list)
'''
list uses square brackets []
tuple uses normal brackets ()
set uses curly brackets {}
'''
'''operations in set'''
#add
set1.add('joy')
print(set1)
set1.add(4)
print(set1)
set1.add('jide')
print(set1)
set1.remove('apple')
print(set1)
'''set doesnt recognise index'''
print(len(set1))
set1.clear() #a bracket must follow every function for it to work eg set1.clear()
print(set1)

yoruba_foods = {'rice','beans','ewedu','salad','fish','egusi'}
igbo_foods = {'egusi','bitter leaf','rice','beans','banga'}
union_set = yoruba_foods | igbo_foods
print(union_set)
interset_set = yoruba_foods & igbo_foods
print(interset_set)

'''user_names = list(input('input random letters'))
print(user_names)
non_duplicate = set(user_names)
print(non_duplicate)'''

signed_up_users = {'user1','user2','user3','user4','user5'}
logged_in_users = {'user1','user3','user5'}
active_users = signed_up_users & logged_in_users
print(active_users)

'''
dictionary this is an unordered collections of items that stores data in key value pair
'''
#jide_details is the dictionary name in this case
jide_details = {
    'username' : 'jkbrime',
    'password' : 1441,
    'email' : 'jkbrime@yahoo.com'
}

print(jide_details)
jide_username = jide_details['username']
print(jide_username)
jide_password = jide_details['password']
print(jide_password)
jide_email = jide_details['email']
print(jide_email)
#to add other data eg id

jide_details['id_number'] = 4119
print(jide_details)

#to change password

jide_details['password'] = 14411
print(jide_details)

#to delete
del jide_details['email']
print(jide_details)
