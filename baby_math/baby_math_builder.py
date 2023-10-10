# my Day 2 project in python
print("Welcome to the sm@i software\t\there we build calculation skill.")
print("Input your name")
user_name = input()
print("Tell us your calculation level\t\tJust to know what to prepare for you.")
print("0.A Beginner level\n1.An Intermediate level\n2.A professional level\n3.A Machine level")
user_level = int(input())
if user_level == 0:
    print("---[" + user_name + "]--- here you are at the beginner's level of calculation")
    import random
    continue_status = 1
    score_detail = 0
    plus_score = 0
    minus_score = 0
    while continue_status:
        random_no1 = random.randrange(0, 10)
        random_no2 = random.randrange(4, 10)
        choose_sign = random.randrange(1, 4)

        if choose_sign == 1:
            print("\t\t\tadd --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 + random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                print("The correct Ans is --[{}]--".format(random_no1 + random_no2))
            print("\t\t1 to continue an 0 to Quit")
            continue_status = int(input())
            if continue_status != 0 and continue_status != 1:
                print("Error in the input")
                break
        elif choose_sign == 2:
            print("\t\t\tSubtract --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 - random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                print("The correct Ans is --[{}]--".format(random_no1 - random_no2))
            print("\t\t1 to continue an 0 to Quit")
            continue_status = int(input())
            if continue_status != 0 and continue_status != 1:
                print("Error in the input")
                break
        elif choose_sign == 3:
            print("\t\t\tMultiply --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 * random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                print("The correct Ans is --[{}]--".format(random_no1 * random_no2))
            print("\t\t1 to continue an 0 to Quit")
            continue_status = int(input())
            if continue_status != 0 and continue_status != 1:
                print("Error in the input")
                break
        elif choose_sign == 4:
            print("\t\t\tDivide --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 / random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                my_ans = (random_no1 / random_no2)
                if my_ans % 1 != 0:
                    print("The correct Ans is --[{}]--".format(float(my_ans)))
                else:
                    print("The correct Ans is --[{}]--".format(my_ans))
                print("\t\t1 to continue and 0 to Quit")
                continue_status = int(input())
                if continue_status != 0 and continue_status != 1:
                    print("Error in the input")
                    break
    score_detail = plus_score + minus_score
    percentage = float((plus_score / score_detail) * 100)
    print("\n\t\t\t\t\t{}, Here is you score details".format(user_name.upper()))
    print("Total number of Questions Solved: ---[{}]---".format(score_detail))
    print("Total number of Correctly answered Questions: ---[{}]---".format(plus_score))
    print("Total number of Wrongly answered Questions: ---[{}]---".format(minus_score))
    print("You have a percentage Score of ---[{}%]---".format(percentage))
elif user_level == 1:
    print("---[" + user_name + "]--- here you are at the intermediate's level of calculation")
    import random
    continue_status = 1
    score_detail = 0
    plus_score = 0
    minus_score = 0
    while continue_status:
        random_no1 = random.randrange(50, 200)
        random_no2 = random.randrange(100, 300)
        choose_sign = random.randrange(1, 4)

        if choose_sign == 1:
            print("\t\t\tadd --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 + random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                print("The correct Ans is --[{}]--".format(random_no1 + random_no2))
            print("\t\t1 to continue an 0 to Quit")
            continue_status = int(input())
            if continue_status != 0 and continue_status != 1:
                print("Error in the input")
                break
        elif choose_sign == 2:
            print("\t\t\tSubtract --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 - random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                print("The correct Ans is --[{}]--".format(random_no1 - random_no2))
            print("\t\t1 to continue an 0 to Quit")
            continue_status = int(input())
            if continue_status != 0 and continue_status != 1:
                print("Error in the input")
                break
        elif choose_sign == 3:
            print("\t\t\tMultiply --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 * random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                print("The correct Ans is --[{}]--".format(random_no1 * random_no2))
            print("\t\t1 to continue an 0 to Quit")
            continue_status = int(input())
            if continue_status != 0 and continue_status != 1:
                print("Error in the input")
                break
        elif choose_sign == 4:
            print("\t\t\tDivide --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 / random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                my_ans = (random_no1 / random_no2)
                if my_ans % 1 != 0:
                    print("The correct Ans is --[{}]--".format(float(my_ans)))
                else:
                    print("The correct Ans is --[{}]--".format(my_ans))
                print("\t\t1 to continue an 0 to Quit")
                continue_status = int(input())
                if continue_status != 0 and continue_status != 1:
                    print("Error in the input")
                    break
    score_detail = plus_score + minus_score
    percentage = float((plus_score / score_detail) * 100)
    print("\n\t\t\t\t\t{}, Here is you score details".format(user_name.upper()))
    print("Total number of Questions Solved: ---[{}]---".format(score_detail))
    print("Total number of Correctly answered Questions: ---[{}]---".format(plus_score))
    print("Total number of Wrongly answered Questions: ---[{}]---".format(minus_score))
    print("You have a percentage Score of ---[{}%]---".format(percentage))

elif user_level == 2:
    print("---[" + user_name + "]--- here you are at the Professional's level of calculation")
    import random
    continue_status = 1
    score_detail = 0
    plus_score = 0
    minus_score = 0
    while continue_status:
        random_no1 = random.randrange(200, 1000)
        random_no2 = random.randrange(500, 1000)
        choose_sign = random.randrange(1, 4)

        if choose_sign == 1:
            print("\t\t\tadd --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 + random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                print("The correct Ans is --[{}]--".format(random_no1 + random_no2))
            print("\t\t1 to continue an 0 to Quit")
            continue_status = int(input())
            if continue_status != 0 and continue_status != 1:
                print("Error in the input")
                break
        elif choose_sign == 2:
            print("\t\t\tSubtract --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 - random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                print("The correct Ans is --[{}]--".format(random_no1 - random_no2))
            print("\t\t1 to continue an 0 to Quit")
            continue_status = int(input())
            if continue_status != 0 and continue_status != 1:
                print("Error in the input")
                break
        elif choose_sign == 3:
            print("\t\t\tMultiply --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 * random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                print("The correct Ans is --[{}]--".format(random_no1 * random_no2))
            print("\t\t1 to continue an 0 to Quit")
            continue_status = int(input())
            if continue_status != 0 and continue_status != 1:
                print("Error in the input")
                break
        elif choose_sign == 4:
            print("\t\t\tDivide --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 / random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                my_ans = (random_no1 / random_no2)
                if my_ans % 1 != 0:
                    print("The correct Ans is --[{}]--".format(float(my_ans)))
                else:
                    print("The correct Ans is --[{}]--".format(my_ans))
                print("\t\t1 to continue an 0 to Quit")
                continue_status = int(input())
                if continue_status != 0 and continue_status != 1:
                    print("Error in the input")
                    break
    score_detail = plus_score + minus_score
    percentage = float((plus_score / score_detail) * 100)
    print("\n\t\t\t\t\t{}, Here is you score details".format(user_name.upper()))
    print("Total number of Questions Solved: ---[{}]---".format(score_detail))
    print("Total number of Correctly answered Questions: ---[{}]---".format(plus_score))
    print("Total number of Wrongly answered Questions: ---[{}]---".format(minus_score))
    print("You have a percentage Score of ---[{}%]---".format(percentage))

elif user_level == 3:
    print("---[" + user_name + "]--- here you are at the machine's level of calculation")
    import random
    continue_status = 1
    score_detail = 0
    plus_score = 0
    minus_score = 0
    while continue_status:
        random_no1 = random.randrange(11191, 100092)
        random_no2 = random.randrange(50064, 100064)
        choose_sign = random.randrange(1, 4)

        if choose_sign == 1:
            print("\t\t\tadd --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 + random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                print("The correct Ans is --[{}]--".format(random_no1 + random_no2))
            print("\t\t1 to continue an 0 to Quit")
            continue_status = int(input())
            if continue_status != 0 and continue_status != 1:
                print("Error in the input")
                break
        elif choose_sign == 2:
            print("\t\t\tSubtract --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 - random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                print("The correct Ans is --[{}]--".format(random_no1 - random_no2))
            print("\t\t1 to continue an 0 to Quit")
            continue_status = int(input())
            if continue_status != 0 and continue_status != 1:
                print("Error in the input")
                break
        elif choose_sign == 3:
            print("\t\t\tMultiply --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 * random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                print("The correct Ans is --[{}]--".format(random_no1 * random_no2))
            print("\t\t1 to continue an 0 to Quit")
            continue_status = int(input())
            if continue_status != 0 and continue_status != 1:
                print("Error in the input")
                break
        elif choose_sign == 4:
            print("\t\t\tDivide --[{}]-- and --[{}]--".format(random_no1, random_no2))
            user_ans = int(input())
            if user_ans == (random_no1 / random_no2):
                plus_score += 1
                print("Correct")
            else:
                minus_score += 1
                print("Sorry " + user_name + " You are wrong")
                my_ans = (random_no1 / random_no2)
                if my_ans % 1 != 0:
                    print("The correct Ans is --[{}]--".format(float(my_ans)))
                else:
                    print("The correct Ans is --[{}]--".format(my_ans))
                print("\t\t1 to continue an 0 to Quit")
                continue_status = int(input())
                if continue_status != 0 and continue_status != 1:
                    print("Error in the input")
                    break
    score_detail = plus_score + minus_score
    percentage = float((plus_score / score_detail) * 100)
    print("\n\t\t\t\t\t{}, Here is you score details".format(user_name.upper()))
    print("Total number of Questions Solved: ---[{}]---".format(score_detail))
    print("Total number of Correctly answered Questions: ---[{}]---".format(plus_score))
    print("Total number of Wrongly answered Questions: ---[{}]---".format(minus_score))
    print("You have a percentage Score of ---[{}%]---".format(percentage))

else:
    print("\nInput Error\nSorry try again.")
