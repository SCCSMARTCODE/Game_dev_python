import random as selector
import os
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\tWelcome to the word cookies game dev")
print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t@smai")


# life box
def life_box(life):
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t        life box")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t---------------")
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    | {} {} {} {} |".format(life[0], life[1], life[2], life[3]))
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t    | {} {} {} {} |".format(life[4], life[5], life[6], life[7]))
    print("\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t---------------")


print("Input your user name: ", end='')
user_name = input()
print("\n\n")
level = 1
co_level = "yes"
while 1:
    if co_level.lower() == 'no':
        break


    def dict_four():
        word_box0 = ["zero", "area", "beak", "calm", "dawn", "even", "fume", "grip", "helm", "iris"]
        word_box111 = ["jump", "kite", "lime", "maze", "note", "opal", "pine", "quiz", "rose", "slug"]
        word_box21 = ["tree", "urge", "vain", "west", "xeno", "yoga", "zing", "axis", "bark", "cake"]
        word_box3 = ["duck", "exit", "fire", "goat", "hero", "iron", "jury", "lamp", "moon", "nail"]
        word_box4 = ["able", "back", "card", "dart", "each", "fact", "gold", "hike", "jazz", "kite"]
        word_box5 = ["luck", "milk", "note", "open", "pink", "quiz", "ride", "soap", "true", "vast"]
        word_box6 = ["wave", "clay", "yell", "zero", "band", "cake", "deer", "fish", "goat", "harp"]
        word_box7 = ["icon", "jump", "knee", "lamp", "moon", "nose", "oath", "peel", "quiz", "ring"]
        word_box8 = ["star", "tree", "urge", "vent", "walk", "xeno", "yawn", "zeal", "axis", "bend"]
        word_box9 = ["care", "dock", "fern", "gulp", "hush", "iron", "jolt", "kite", "lime", "muse"]
        word_box10 = ["nail", "opal", "plum", "quay", "rose", "slug", "tide", "urge", "vain", "west"]
        word_box11 = ["xeno", "yoga", "zing", "atom", "blue", "chop", "duck", "exit", "fear", "gaze"]
        word_box12 = ["hike", "isle", "jury", "kite", "lava", "mole", "note", "opal", "pine", "quiz"]
        word_box13 = ["ride", "salt", "tent", "urge", "vast", "wine", "xeno", "yawn", "zeal", "axis"]
        word_box14 = ["bark", "cake", "dust", "fire", "goat", "hero", "iron", "jolt", "knee", "lamp"]
        word_box15 = ["moon", "nail", "opal", "plum", "quiz", "rose", "star", "tide", "urge", "vent"]
        word_box_four = []
        word_box_four_extend = []

        word_box_four += word_box0, word_box111, word_box21, word_box3, word_box4, word_box5, word_box6, word_box7
        word_box_four += word_box8, word_box9, word_box10, word_box11, word_box12, word_box13, word_box14, word_box15
        loop_in = 0
        while loop_in <= 15:
            word_box_four_extend.extend(word_box_four[loop_in])
            loop_in += 1
        return word_box_four_extend


    def dict_other():
        wordbox0 = ["apple", "brave", "crane", "dwell", "eager", "flame", "grape", "happy", "icicle", "jolly"]
        wordbox1 = ["knack", "lemon", "melon", "noble", "ocean", "piano", "quilt", "ruler", "sweep", "table"]
        wordbox2 = ["unity", "vivid", "waste", "xenon", "yield", "zebra", "agile", "blink", "chase", "dance"]
        wordbox3 = ["evoke", "fable", "glide", "haste", "image", "jewel", "knock", "latch", "muddy", "noble"]
        wordbox4 = ["opera", "plumb", "quiet", "rebel", "swirl", "tramp", "uncle", "vivid", "wrist", "xerox"]
        wordbox5 = ["yield", "zebra", "acorn", "baker", "champ", "drown", "eleven", "flint", "grain", "happy"]
        wordbox6 = ["ivory", "joker", "knife", "leash", "magic", "night", "oasis", "pluto", "quart", "rider"]
        wordbox7 = ["sable", "torch", "under", "vault", "watch", "xylophone", "yellow", "zeppelin", "almond", "butter"]
        wordbox8 = ["carpet", "dazzle", "eighty", "flock", "guitar", "humble", "invent", "juggle", "knight", "laugh"]
        wordbox9 = ["magnet", "novel", "oyster", "plaque", "quiver", "rocket", "snail", "thirty", "umbra", "vortex"]
        wordbox10 = ["wizard", "xylophone", "cactus", "dragon", "elephant", "fizzle", "guitar", "humble", "imagine", "jungle"]
        wordbox11 = ["knight", "lemon", "monsoon", "octopus", "parade", "quilt", "rocket", "sailor", "thunder", "unicorn"]
        wordbox12 = ["volcano", "whistle", "xylophone", "yacht", "zeppelin", "accordion", "butterfly", "champion", "dragonfly", "elephant"]
        wordbox13 = ["festival", "gorilla", "honeycomb", "jackpot", "kangaroo", "leopard", "moonlight", "nightmare", "octagon", "paradise"]
        wordbox14 = ["quicksand", "rhinoceros", "starlight", "thunderstorm", "universe", "volleyball", "waterfall", "xylophone", "yellowstone", "zeppelin"]
        wordbox15 = ["accompany", "blossom", "candlelight", "delightful", "effortless", "fascinate", "grandfather", "happiness", "incredible", "jubilant"]
        word_box_five = []
        word_box_five_extend = []

        word_box_five += wordbox0, wordbox1, wordbox2, wordbox3, wordbox4, wordbox5, wordbox6, wordbox7
        word_box_five += wordbox8, wordbox9, wordbox10, wordbox11, wordbox12, wordbox13, wordbox14, wordbox15
        loop_in = 0
        while loop_in <= 15:
            word_box_five_extend.extend(word_box_five[loop_in])
            loop_in += 1
        return word_box_five_extend

    word_box = ["smart", "exited", "kindness"]
    word_box1 = dict_four()
    word_box2 = dict_other()

    word_box.extend(word_box1)
    word_box.extend(word_box2)

    life_box_reader = ['*', '*', '*', '*', '*', '*', '*', '*']
    life_box_reader_index = 0
    selected_word = selector.choice(word_box)
    temp_selected_word = []
    for x in selected_word:
        temp_selected_word.append(x)
    a = 0
    while a < len(temp_selected_word):
        temp_selected_word[a] = '_'
        a += 1
    while 1:
        if life_box_reader_index > 0:
            life_box_reader[life_box_reader_index - 1] = '-'
        if "_" in temp_selected_word:
            pass
        else:
            print(temp_selected_word)
            print("------------------------Thanks for completing this level------------------\n\n")
            level += 1
            while 1:
                co_level = input("Are you ready to fill in the next missing letters [--yes or no--] ")
                if co_level.lower() == 'yes' or co_level.lower() == 'no':
                    break
            if co_level.lower() == 'yes':
                os.system('cls')
            else:
                print("--------------------thank you {}".format(user_name))
                break
            print("\t\t\t\t\t\t\t\t\t------------------------ welcome to level {} ------------------------\n\n".format(level))
            break
            # print(life_box_reader)
        b = 0
        run = 1
        for x in temp_selected_word:
            if x != '_':
                run *= 0
            else:
                run *= 1
        if run == 1 and len(selected_word) <= 4:
            help_solve = selector.randint(1, len(selected_word))
            temp_selected_word[help_solve - 1] = selected_word[help_solve - 1]

        elif run == 1 and len(selected_word) <= 6:
            help_solve1 = selector.randint(1, len(selected_word))
            new_help_solve_list = [x for x in range(1, len(selected_word) + 1) if x != help_solve1]
            help_solve2 = selector.choice(new_help_solve_list)

            temp_selected_word[help_solve1 - 1] = selected_word[help_solve1 - 1]
            temp_selected_word[help_solve2 - 1] = selected_word[help_solve2 - 1]

        elif run == 1 and len(selected_word) >= 7:
            help_solve1 = selector.randint(1, len(selected_word))
            new_help_solve_list = [x for x in range(1, len(selected_word) + 1) if x != help_solve1]
            help_solve2 = selector.choice(new_help_solve_list)
            new_help_solve_list1 = [x for x in range(1, len(selected_word) + 1) if x != help_solve1 and x != help_solve2]
            help_solve3 = selector.choice(new_help_solve_list1)

            temp_selected_word[help_solve1 - 1] = selected_word[help_solve1 - 1]
            temp_selected_word[help_solve2 - 1] = selected_word[help_solve2 - 1]
            temp_selected_word[help_solve3 - 1] = selected_word[help_solve3 - 1]
 
        print("\nFill in the missing letter.")
        for x in selected_word:
            print("[{}]".format(temp_selected_word[b]), end="")
            b += 1

        life_box(life_box_reader)

        # user input and all it's checks
        print("input a letter to fill in the missing spaces\t\t\t\t\t\t\t for assistance input [--help--]")
        user_guess = input()
        if user_guess.lower() == "exit":
            co_level = "no"
            break
        if user_guess.lower() == "help":
            print("What box number should i update e.g--->>> 1 or 2 or .....")
            update_num = input()
            if update_num not in "0123456789":
                print("Invalid input")
                continue
            else:
                update_num = int(update_num)
            if 1 > update_num > len(selected_word):
                print("update invalid")
                continue
            elif update_num in range(1, len(selected_word) + 1):
                if temp_selected_word[update_num - 1] == selected_word[update_num - 1]:
                    print("No new update")
                    continue
                else:
                    temp_selected_word[update_num - 1] = selected_word[update_num - 1]
                    life_box_reader_index += 1
                    continue
            else:
                print("Error update ....")
                continue
        while 1:
            if len(user_guess) == 0:
                print("input")
                user_guess = input()
            else:
                break
        if len(user_guess) != 1:
            print("You are allowed to input one character at a time")
            life_box_reader_index += 1
            continue

        alpha = "abcdefghijklmnopqrstuvwxyz"
        if user_guess not in alpha:
            print("invalid input")
            life_box_reader_index += 1
            continue
        index_input_position = 0
        pass_in = 0
        for x in selected_word:
            if user_guess.lower() == x:
                if temp_selected_word[index_input_position] == '_':
                    pass_in = 1
                    break

                # elif temp_selected_word[index_input_position] != '_':
                #     continue
            index_input_position += 1
        if "_" in temp_selected_word:
            if pass_in == 1:
                temp_selected_word[index_input_position] = user_guess.lower()
            else:
                life_box_reader_index += 1
                if life_box_reader_index >= 8:
                    print("------------------------------------life box empty")
                    print("------------------------------------You lose")
                    print("the uncompleted word is --[{}]--".format(selected_word), "\n\n")
                    co_level = "no"
                    break
