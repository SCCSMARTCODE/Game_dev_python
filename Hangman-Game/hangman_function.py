import random as select
"""This is a module
        that contain the several functions
            that will be running the Hand Man Game"""


def hang_structure(lose=0):
    """This is my hang man structure function
            This will keep updating as the game continues
    """

    lose_table_update = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    lose_table = ["|", "O", "|", "\\", "/", "|", "|", "\\", "/"]
    i = 0
    while i < lose:
        lose_table_update[i] = lose_table[i]
        i += 1

    print("\t===========")
    print("\t|        {}".format(lose_table_update[0]))
    print("\t|        {}".format(lose_table_update[1]))
    print("\t|       {}{}{}".format(lose_table_update[3], lose_table_update[2], lose_table_update[4]))
    print("\t|        {}".format(lose_table_update[5]))
    print("\t|       {}{}{}".format(lose_table_update[8], lose_table_update[6], lose_table_update[7]))
    print("\t|")
    print("\t|")
    print(" -------")


def guessed_letter_tracker(guessed_letter_box, letter):
    """This is the function responsible
        for more than once selection of a
            particular letter"""

    let_str = str(letter)
    if let_str.upper() in guessed_letter_box or let_str.lower() in guessed_letter_box:
        print("Sorry, you already guessed `{}`".format(letter))
        return False
    guessed_letter_box.append(letter)
    return guessed_letter_box


def word_to_guess():
    words = ['Man', 'Knock', 'Smart', 'Thanks', 'Ring', 'Fame', 'Grace', 'HangMan']
    guess_this = select.choice(words)
    return guess_this
