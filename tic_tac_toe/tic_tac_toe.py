import box_structure as box
import pass_input as win


def empty_name_check(name):
    while len(name) == 0:
        name = input("Zero buffer: Error\nInput your game user name: ")
    return name


def inner_space_to_underscore(name):
    name = str(name)
    name = name.replace(" ", "_")
    return name


print("\t\t\t\t\t\t\t\t\t\t\t----------------------------@smai.com-----------------------------")
game_play_mode = 0
while game_play_mode not in ['1', '2']:
    game_play_mode = input("Game_Mode[_]:\n\t1. Computer as opponent\n\t2. Multiplayer\n\t\tInput mode: ")
print("Game_Mode[{}] Selected".format(game_play_mode))

user_name1 = input("Input your name player 1: ")
user_name1 = empty_name_check(user_name1)
user_name1 = inner_space_to_underscore(user_name1)
if game_play_mode == '2':
    user_name2 = input("Input your name player 2: ")
else:
    Computer_name = 'SM@I'
    if user_name1 == Computer_name:
        Computer_name = "SM@RT"
    user_name2 = Computer_name
    print("\nNice to meet you {}\n\tMy Name is {} i am you opponent".format(user_name1, user_name2))
user_name2 = empty_name_check(user_name2)
user_name2 = inner_space_to_underscore(user_name2)
while user_name2 == user_name1:
    user_name2 = input("\nsorry-->>\nThe user name: --[{}]-- is no more available\nInput another user name: ".format(user_name2))

print("\t\t\t\t\t\t\t\t________________Welcome {} and {}, to the tic-tac-toe--game-dev @smai.com____________________".format(user_name1, user_name2))


def check_empty_buffer(user_buffer):
    while len(user_buffer) == 0:
        user_buffer = input("Zero input\nYou are expected to select a number: ")
    else:
        return user_buffer


def call():
    p_1 = input()
    p_1 = check_empty_buffer(p_1)
    while p_1 not in "123456789":
        print("\nInvalid input\nYou are to input the box number selected\ne.g ---------1,2,3,4,5,6,7,8,9----------")
        print("Input a valid value: ", end='')
        p_1 = call()
    return int(p_1)


def check_position(per_call, person):
    equation_list = [box.filled_list1, box.filled_list2]
    if box.full_empty_box[per_call - 1][2] == ' ':
        box.full_empty_box[per_call - 1] = equation_list[person]
    else:
        print("\nThis space as been filled up\nchoose another box")
        note_that = call()
        check_position(note_that, person)


def check_empty_space():
    i = 0
    j = 0
    while i < len(box.full_empty_box):
        if " " == box.full_empty_box[i][3]:
            j += 1
        i += 1

    if j == 0:
        print("\n\t\t------------------------\n\t\t\t\t\tAt the end of the Nobody breaks the Box\t--------------------\nThat is bad so no winner\nSee you at the next competition")
        exit(0)


box.box1(box.full_empty_box)
while 1:
    # first man
    print("{}, pick your box number".format(user_name1))
    check_call1 = call()
    check_position(check_call1, 0)
    box.box3(box.full_empty_box)
    # check right
    the_winner_is_1 = win.winner_checker(box.full_empty_box)
    if the_winner_is_1 == 1:
        print("\t\t\t\t\t\t\t\t\t\t-------------------------- {} is the next expected winner--------------------------".format(user_name2))
    else:
        print("\n\n\t\t\t\t\t\t\t\t\t\t{} is the lucky winner for this champion game".format(user_name1))
        print("\t\t\t\t\t\t\t\t\t\t--------------------------The lucky box has been home by the Second player--[{}]".format(user_name1))
        box.box3(box.full_empty_box)
        print("\n\n\t\t\t--------------------------{} is definitely a good player but...forget it, {} crushed {}".format(user_name2, user_name1, user_name2))
        print("\n\n\t\t\t\t\t---------------------------------Thank you see you at the next run time---------------------------------")
        exit(0)
    check_empty_space()

    # second man
    print("{}, pick your box number".format(user_name2))
    if game_play_mode == '1':
        check_call2 = win.computer_brain_base(check_call1, box.full_empty_box)
    else:
        check_call2 = call()
    check_position(check_call2, 1)
    box.box3(box.full_empty_box)
    # check right
    the_winner_is_2 = win.winner_checker(box.full_empty_box)
    if the_winner_is_2 == 1:
        print("\t\t\t\t\t\t\t\t\t\t-------------------------- {} is the next expected winner--------------------------".format(user_name1))
    else:
        print("\n\n\t\t\t\t\t\t\t\t\t\t{} is the lucky winner for this champion game".format(user_name2))
        print("\t\t\t\t\t\t\t\t\t\t--------------------------The lucky box has been owned by the Second player--[{}]".format(user_name2))
        box.box3(box.full_empty_box)
        print("\n\n\t\t\t--------------------------{} is definitely a good player but ... forget it, {} crushed {}".format(user_name1, user_name2, user_name1))
        print("\n\n\t\t\t\t\t---------------------------------Thank you see you at the next run time---------------------------------")
        exit(0)
    check_empty_space()
