#!/usr/bin/python3
"""Ask five questions with input(), store answers in a dictionary, comment on them."""


def comment(answers):
    """Print a comment on each answer in the dictionary."""
    print("\nHello " + answers["name"] + "!")

    if answers["age"].isdigit() and int(answers["age"]) < 30:
        print("Young and keen!")
    else:
        print("Wise and experienced!")

    print(answers["colour"] + " is a lovely colour.")

    if answers["python"].lower() == "yes":
        print("Great - you're on the right course!")
    else:
        print("Give it time, it grows on you.")

    if answers["flat"].lower() == "false":
        print("Correct, the world is round!")
    else:
        print("Hmm, NASA would disagree.")


name = input("What is your name? ")
age = input("How old are you? ")
colour = input("What is your favourite colour? ")
python = input("Do you like Python? (yes/no) ")
flat = input("The world is flat: True or False? ")

answers = {"name": name, "age": age, "colour": colour,
           "python": python, "flat": flat}

comment(answers)
