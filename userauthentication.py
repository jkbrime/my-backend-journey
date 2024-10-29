# user = {}

# def register():
#     username = input('enter your username')
#     if username in user:
#      print('username already exist')
#     return


# password = input('enter your password')
# user['username'] = password
# print('registratin done')

user = {
    'user_name': 'olajide buraimoh',
    'password': 1441
}

def register():
    user_name = input('enter a user name')
    if user_name in user:
        print('pick another name')
        return
    full_name = input('enter your full name')
    password_1 = input('enter your password')
    user['user_name'] = {'fullName': full_name, 'password': password_1}
    print('you have successfully registered')
    print(user)

#login function
def login():
    if not user:
        print('user have not registered')
        return
        userName = input('enter your user name')
        password = input('enter your password')
    if user.get(user_name) and user[user_name]['password'] == password:
     print(f'welcome {user['user_name']['fullname']}')

def main():
    current_user = None
    while True:
        print('\n option register login quit')
        choice = input('input an option').lower()

        if choice == 'register':
            register()
        elif choice == 'login':
            login()
        elif choice == 'quit':
            ('stopping program')
        else:
            print('invalid input')

main()
