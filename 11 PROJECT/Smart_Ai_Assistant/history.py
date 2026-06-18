from datetime import datetime


def save_history(user_name, user_input, bot_reply):

    filename = f"history/{user_name}_history.txt"

    with open(filename, "a") as file:

        file.write("\n---------------------\n")

        file.write("Time : ")

        file.write(str(datetime.now()))

        file.write("\n")

        file.write("User : ")

        file.write(user_input)

        file.write("\n")

        file.write("Bot : ")

        file.write(bot_reply)

        file.write("\n")