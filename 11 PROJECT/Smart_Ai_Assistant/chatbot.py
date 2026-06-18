import json


def load_knowledge():

    try:

        with open("data/knowledge.json", "r") as file:

            return json.load(file)

    except:

        return {}


def save_knowledge(data):

    with open("data/knowledge.json", "w") as file:

        json.dump(data, file, indent=4)


def get_response(user_question):

    data = load_knowledge()

    user_question = user_question.lower()

    for question in data:

        if question in user_question:

            return data[question]

    return "I don't know this. Teach me using 'teach' command."


def teach_bot():

    data = load_knowledge()

    question = input("Question : ").lower()

    answer = input("Answer : ")

    data[question] = answer

    save_knowledge(data)

    print("New knowledge added.")