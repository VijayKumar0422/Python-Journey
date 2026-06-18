from chatbot import get_response, teach_bot
from calculator import calculate
from quotes import get_quote
from jokes import get_joke
from history import save_history

from todo import add_task, show_tasks, delete_task
from notes import add_note, show_notes, delete_note
from memory import remember, recall
from games import guess_number, rock_paper_scissors
from password_generator import generate_password
from date_time import current_date, current_time
from statistics import show_stats

print("=" * 50)
print("SMART AI PERSONAL ASSISTANT")
print("=" * 50)

user_name = input("Enter your name : ")

while True:

    user_input = input(f"{user_name} : ").lower()

    if user_input == "bye":

        bot_reply = "Goodbye"

        print("Bot :", bot_reply)

        save_history(user_name, user_input, bot_reply)

        break

    elif user_input == "quote":

        bot_reply = get_quote()

        print("Bot :", bot_reply)

        save_history(user_name, user_input, bot_reply)

    elif user_input == "joke":

        bot_reply = get_joke()

        print("Bot :", bot_reply)

        save_history(user_name, user_input, bot_reply)

    elif user_input == "calculator":

        expression = input("Enter expression : ")

        bot_reply = str(calculate(expression))

        print("Answer :", bot_reply)

        save_history(user_name, expression, bot_reply)

    elif user_input == "teach":

        teach_bot()

        save_history(user_name, "teach", "New knowledge added")

    elif user_input == "add task":

        add_task()

    elif user_input == "show task":

        show_tasks()

    elif user_input == "delete task":

        delete_task()

    elif user_input == "add note":

        add_note()

    elif user_input == "show note":

        show_notes()

    elif user_input == "delete note":

        delete_note()

    elif user_input == "remember":

        remember()

    elif user_input == "recall":

        recall()

    elif user_input == "guess game":

        guess_number()

    elif user_input == "rps":

        rock_paper_scissors()

    elif user_input == "password":

        length = int(input("Password length : "))

        print("Generated Password :", generate_password(length))

    elif user_input == "date":

        print(current_date())

    elif user_input == "time":

        print(current_time())

    elif user_input == "stats":

        show_stats()

    elif user_input == "help":

        print("""
Available Commands

hello
how are you
quote
joke
calculator
teach
add task
show task
delete task
add note
show note
delete note
remember
recall
guess game
rps
password
date
time
stats
bye
""")

    else:

        bot_reply = get_response(user_input)

        print("Bot :", bot_reply)

        save_history(user_name, user_input, bot_reply)
