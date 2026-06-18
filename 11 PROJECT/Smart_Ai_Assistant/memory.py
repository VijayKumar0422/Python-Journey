import json


def load_memory():

    try:

        with open("data/memory.json", "r") as file:

            return json.load(file)

    except:

        return {}


def save_memory(data):

    with open("data/memory.json", "w") as file:

        json.dump(data, file, indent=4)


def remember():

    data = load_memory()

    key = input("What do you want me to remember? : ").lower()

    value = input("Enter value : ")

    data[key] = value

    save_memory(data)

    print("Memory saved successfully.")


def recall():

    data = load_memory()

    key = input("What should I recall? : ").lower()

    if key in data:

        print("Memory :", data[key])

    else:

        print("Nothing found.")