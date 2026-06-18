import json


def load_notes():

    try:

        with open("data/notes.json", "r") as file:

            return json.load(file)

    except:

        return []


def save_notes(notes):

    with open("data/notes.json", "w") as file:

        json.dump(notes, file, indent=4)


def add_note():

    notes = load_notes()

    note = input("Enter note : ")

    notes.append(note)

    save_notes(notes)

    print("Note saved successfully.")


def show_notes():

    notes = load_notes()

    if len(notes) == 0:

        print("No notes found.")

    else:

        print("\nNotes")

        for index, note in enumerate(notes, start=1):

            print(index, ".", note)


def delete_note():

    notes = load_notes()

    show_notes()

    if len(notes) == 0:

        return

    number = int(input("Enter note number : "))

    notes.pop(number - 1)

    save_notes(notes)

    print("Note deleted.")