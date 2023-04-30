import re
import json
from projectList import projectList

# User class


class User:
    # registration function to get user info and store it in JSON format
    def registiration(self, users_file):
        # get user input for first name, last name, email, password, and mobile number
        self.first_name = input('First Name: ').capitalize()
        self.last_name = input('Last Name: ').capitalize()
        self.Email = input('Email: ')
        self.validate_mail()
        self.password = input('Password: ')
        self.validate_pass()
        self.confirm_password = input('Confirm Password: ')
        self.validate_confirm_pass()
        self.mobile_phone = input('Mobile Phone: ')
        self.validate_mobile()

        # store user info in a dictionary
        user_info = {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "Email": self.Email,
            "password": self.password,
            "mobile_phone": self.mobile_phone
        }

        # write user info to the users file in JSON format
        json.dump(user_info, users_file)
        users_file.write('\n')
        print("=====================")
        print("your registration was successful")

    # login function to check if user exists and validate password

    def login(self, users_file):
        # get user input for email and password
        self.Email = input('Email: ')
        self.password = input('Password: ')
        users_file.seek(0)
        # loop through each line in the users file
        for line in users_file:
            user_info = json.loads(line)
            # check if the entered email and password match an existing user
            if user_info['Email'] == self.Email and user_info['password'] == self.password:
                print(2*"=====================")
                print(f"Welcome {user_info['first_name']}")
                # call the projectList function with the user's email as an argument
                projectList(self.Email)
                return True
        print(2*"=====================")
        print("Invalid email or password")
        return False

    # function to validate email format and check if it already exists in the users file
    def validate_mail(self):
        email_regex = r'^[a-zA-Z0-9._]{6,22}@[a-zA-Z]{5,8}[.]{1}[a-zA-Z.]{3,6}$'
        while True:
            if re.match(email_regex, self.Email):
                with open("users.json", "r") as users_file:
                    for line in users_file:
                        user_info = json.loads(line)
                        if user_info['Email'] == self.Email:
                            print(2*"=====================")
                            print("Email already exists.")
                            print(2*"=====================")
                            self.Email = input('Email: ')
                            break
                    else:
                        break
                users_file.close()
            else:
                print(2*"=====================")
                print("Invalid email format")
                print(2*"=====================")
                self.Email = input('Email: ')

    # function to validate password length
    def validate_pass(self):
        while True:
            if len(self.password) < 8:
                print(2*"=====================")
                print("Password must be at least 8 characters.")
                print(2*"=====================")
                self.password = input('Password: ')
            else:
                break

    # function to check if password confirmation matches the original password
    def validate_confirm_pass(self):
        while True:
            if self.password != self.confirm_password:
                print(2*"=====================")
                print("Passwords do not match.")
                print(2*"=====================")
                self.confirm_password = input('Confirm Password: ')
            else:
                break

    # function to validate Egyptian mobile number format
    def validate_mobile(self):
        mobile_regex = r'^(011|012|010|015)[0-9]{8}$'
        while True:
            if re.match(mobile_regex, self.mobile_phone):
                break
            else:
                print(2*"=====================")
                print("invalid")
                print(2*"=====================")
                self.mobile_phone = input(
                    'Mobile Phone must be in egy format: ')


while True:  # loop until the user chooses to exit
    # open the users file in append mode
    users_file = open("users.json", "a+")
    # create a User object
    user = User()
    print("=====================")
    print("1. Register\n2. Login\n3. Exit")
    print("=====================")
    command = input("Enter a command number: ")
    print("=====================")
    if command == "1":
        # call the registiration method of the User object
        user.registiration(users_file)
        users_file.close()
    elif command == "2":
        user.login(users_file)  # call the login method of the User object

    elif command == "3":
        print("Exit")
        print("=====================")
        break
    else:
        print("Invalid command")
        print("=====================")
