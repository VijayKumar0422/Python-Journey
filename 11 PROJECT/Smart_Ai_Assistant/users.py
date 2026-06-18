import json


def load_users():

    try:

        with open("data/users.json", "r") as file:

            return json.load(file)

    except:

        return {}


def save_users(users):

    with open("data/users.json", "w") as file:

        json.dump(users, file, indent=4)


def register():

    users = load_users()

    username = input("Enter username : ")

    if username in users:

        print("User already exists.")

        return

    password = input("Enter password : ")

    users[username] = password

    save_users(users)

    print("Registration successful.")


def login():

    users = load_users()

    username = input("Username : ")

    password = input("Password : ")

    if username in users and users[username] == password:

        print("Login Successful")

        return username

    else:

        print("Invalid Username or Password")

        return None