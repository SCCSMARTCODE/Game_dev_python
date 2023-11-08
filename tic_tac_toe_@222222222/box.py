import random


def box_nig(space_list):
    print("-------------------")
    print("|  {}  |  {}  |  {}  |".format(space_list[0], space_list[1], space_list[2]))
    print("-------------------")
    print("|  {}  |  {}  |  {}  |".format(space_list[3], space_list[4], space_list[5]))
    print("-------------------")
    print("|  {}  |  {}  |  {}  |".format(space_list[6], space_list[7], space_list[8]))
    print("-------------------")


def system_brain(list_update):

    # winning perspective
    if list_update[0] == list_update[1] == "0" and list_update[2] == " ":
        return 2
    elif list_update[0] == list_update[2] == "0" and list_update[1] == " ":
        return 1
    elif list_update[2] == list_update[1] == "0" and list_update[0] == " ":
        return 0

    elif list_update[3] == list_update[4] == "0" and list_update[5] == " ":
        return 5
    elif list_update[5] == list_update[4] == "0" and list_update[3] == " ":
        return 3
    elif list_update[3] == list_update[5] == "0" and list_update[4] == " ":
        return 4

    elif list_update[6] == list_update[7] == "0" and list_update[8] == " ":
        return 8
    elif list_update[6] == list_update[8] == "0" and list_update[7] == " ":
        return 7
    elif list_update[8] == list_update[7] == "0" and list_update[6] == " ":
        return 6

    elif list_update[0] == list_update[3] == "0" and list_update[6] == " ":
        return 6
    elif list_update[6] == list_update[3] == "0" and list_update[0] == " ":
        return 0
    elif list_update[0] == list_update[6] == "0" and list_update[3] == " ":
        return 3

    elif list_update[1] == list_update[4] == "0" and list_update[7] == " ":
        return 7
    elif list_update[1] == list_update[7] == "0" and list_update[4] == " ":
        return 4
    elif list_update[7] == list_update[4] == "0" and list_update[1] == " ":
        return 1

    elif list_update[2] == list_update[5] == "0" and list_update[8] == " ":
        return 8
    elif list_update[2] == list_update[8] == "0" and list_update[5] == " ":
        return 5
    elif list_update[8] == list_update[5] == "0" and list_update[2] == " ":
        return 2

    elif list_update[0] == list_update[4] == "0" and list_update[8] == " ":
        return 8
    elif list_update[8] == list_update[4] == "0" and list_update[0] == " ":
        return 0
    elif list_update[0] == list_update[8] == "0" and list_update[4] == " ":
        return 4

    elif list_update[2] == list_update[4] == "0" and list_update[6] == " ":
        return 6
    elif list_update[2] == list_update[6] == "0" and list_update[4] == " ":
        return 4
    elif list_update[6] == list_update[4] == "0" and list_update[2] == " ":
        return 2

    # defence mode
    elif list_update[0] == list_update[1] == "X" and list_update[2] == " ":
        return 2
    elif list_update[0] == list_update[2] == "X" and list_update[1] == " ":
        return 1
    elif list_update[2] == list_update[1] == "X" and list_update[0] == " ":
        return 0

    elif list_update[3] == list_update[4] == "X" and list_update[5] == " ":
        return 5
    elif list_update[5] == list_update[4] == "X" and list_update[3] == " ":
        return 3
    elif list_update[3] == list_update[5] == "X" and list_update[4] == " ":
        return 4

    elif list_update[6] == list_update[7] == "X" and list_update[8] == " ":
        return 8
    elif list_update[6] == list_update[8] == "X" and list_update[7] == " ":
        return 7
    elif list_update[8] == list_update[7] == "X" and list_update[6] == " ":
        return 6

    elif list_update[0] == list_update[3] == "X" and list_update[6] == " ":
        return 6
    elif list_update[6] == list_update[3] == "X" and list_update[0] == " ":
        return 0
    elif list_update[0] == list_update[6] == "X" and list_update[3] == " ":
        return 3

    elif list_update[1] == list_update[4] == "X" and list_update[7] == " ":
        return 7
    elif list_update[1] == list_update[7] == "X" and list_update[4] == " ":
        return 4
    elif list_update[7] == list_update[4] == "X" and list_update[1] == " ":
        return 1

    elif list_update[2] == list_update[5] == "X" and list_update[8] == " ":
        return 8
    elif list_update[2] == list_update[8] == "X" and list_update[5] == " ":
        return 5
    elif list_update[8] == list_update[5] == "X" and list_update[2] == " ":
        return 2

    elif list_update[0] == list_update[4] == "X" and list_update[8] == " ":
        return 8
    elif list_update[8] == list_update[4] == "X" and list_update[0] == " ":
        return 0
    elif list_update[0] == list_update[8] == "X" and list_update[4] == " ":
        return 4

    elif list_update[2] == list_update[4] == "X" and list_update[6] == " ":
        return 6
    elif list_update[2] == list_update[6] == "X" and list_update[4] == " ":
        return 4
    elif list_update[6] == list_update[4] == "X" and list_update[2] == " ":
        return 2

    else:
        pick_list = [x for x in range(0, 9) if list_update[x] == " "]
        return random.choice(pick_list)
