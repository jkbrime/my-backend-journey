# user = {}

# def register():
#     username = input('enter your username')
#     if username in user:
#      print('username already exist')
#     return


# password = input('enter your password')
# user['username'] = password
# print('registratin done')


# Dictionary to store user data
user_data = {}

# Function to register a user
def register():
    username = input("Enter a username: ")
    if username in user_data:
        print("Username already exists. Try a different one.")
        return
    password = input("Enter a password: ")
    user_data[username] = password
    print(f"User '{username}' registered successfully!")

# Function to log in
def login():
    if not user_data:
        print("No users registered. Please register first.")
        return
    username = input("Enter your username: ")
    password = input("Enter your password: ")
    
    if user_data.get(username) == password:
        print(f"Welcome, {username}! You are now logged in.")
        return username
    else:
        print("Invalid username or password. Please try again.")
        return None

# Function to log out
def logout(username):
    if username:
        print(f"Goodbye, {username}! You have successfully logged out.")
        return None
    else:
        print("No user is currently logged in.")

# Main program loop
def main():
    current_user = None
    while True:
        print("\nOptions: register, login, logout, quit")
        choice = input("Choose an option: ").lower()

        if choice == "register":
            register()
        elif choice == "login":
            if current_user:
                print(f"User '{current_user}' is already logged in.")
            else:
                current_user = login()
        elif choice == "logout":
            current_user = logout(current_user)
        elif choice == "quit":
            print("Exiting the program.")
            break
        else:
            print("Invalid option. Please try again.")

# Run the main program
main()



'''
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
'''