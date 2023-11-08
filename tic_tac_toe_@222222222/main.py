import box


def check_picked_space(list_update, u_input):
    if list_update[u_input] != " ":
        print("Sorry this space as been filled up")
        return "Error"
    return u_input


def print_box(list_update):
    box.box_nig(list_update)


def check_input_alignment(u_input):
    while u_input not in "012345678":
        print("Invalid box number")
        u_input = input("Player input your value: ")
    return u_input


def check_empty_input(u_input):
    while len(u_input) == 0:
        u_input = input("Player input your value: ")
    return u_input


def check_winner(list_update):
    if list_update[0] == list_update[1] == list_update[2] != " ":
        return 1
    elif list_update[3] == list_update[4] == list_update[5] != " ":
        return 1
    elif list_update[6] == list_update[7] == list_update[8] != " ":
        return 1
    elif list_update[0] == list_update[3] == list_update[6] != " ":
        return 1
    elif list_update[1] == list_update[4] == list_update[7] != " ":
        return 1
    elif list_update[2] == list_update[5] == list_update[8] != " ":
        return 1
    elif list_update[0] == list_update[4] == list_update[8] != " ":
        return 1
    elif list_update[2] == list_update[4] == list_update[6] != " ":
        return 1
    else:
        return 0


def check_no_winner(list_update):
    if " " in list_update:
        return 1
    else:
        return 0


space_list = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
space_list1 = ["0", "1", "2", "3", "4", "5", "6", "7", "8"]
print_box(space_list1)

while 1:

    # player
    user_input = input("Player input your value: ")
    user_input = check_empty_input(user_input)

    # check 1
    user_input = check_input_alignment(user_input)
    # check 1

    user_input = int(user_input)

    # Check if space picked is available
    user_input = check_picked_space(space_list, user_input)
    # Check if space picked is available

    while user_input == "Error":
        user_input = input("Please input another value: ")
        user_input = check_empty_input(user_input)
        user_input = check_input_alignment(user_input)
        user_input = int(user_input)
        user_input = check_picked_space(space_list, user_input)
    else:
        space_list[user_input] = "X"
    print_box(space_list)

    checking_success = check_winner(space_list)
    if checking_success == 1:
        print("You Win")
        exit(1)
    checking_failure = check_no_winner(space_list)
    if checking_failure == 0:
        print("Thanks, no winner in this Game")
        exit(0)

    # computer selection
    user2_input = box.system_brain(space_list)
    space_list[user2_input] = "0"
    print("The computer selected ----[{}]----".format(user2_input))
    print_box(space_list)
    checking_success = check_winner(space_list)
    if checking_success == 1:
        print("You Lose")
        exit(1)
    checking_failure = check_no_winner(space_list)
    if checking_failure == 0:
        print("Thanks, no winner in this Game")
        exit(0)
