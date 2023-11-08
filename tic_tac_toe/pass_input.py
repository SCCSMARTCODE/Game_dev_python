import random
from box_structure import filled_list2, filled_list1


def winner_checker(score_box):
    winner_checker_value = ["-", "-", "-", "-"]

    if score_box[0] == score_box[1] == score_box[2]:
        score_box[0] = score_box[1] = score_box[2] = winner_checker_value
        return score_box

    elif score_box[3] == score_box[4] == score_box[5]:
        score_box[3] = score_box[4] = score_box[5] = winner_checker_value
        return score_box

    elif score_box[6] == score_box[7] == score_box[8]:
        score_box[6] = score_box[7] = score_box[8] = winner_checker_value
        return score_box

    elif score_box[0] == score_box[4] == score_box[8]:
        score_box[0] = score_box[4] = score_box[8] = winner_checker_value
        return score_box

    elif score_box[2] == score_box[4] == score_box[6]:
        score_box[2] = score_box[4] = score_box[6] = winner_checker_value
        return score_box

    elif score_box[0] == score_box[3] == score_box[6]:
        score_box[0] = score_box[3] = score_box[6] = winner_checker_value
        return score_box

    elif score_box[1] == score_box[4] == score_box[7]:
        score_box[1] = score_box[4] = score_box[7] = winner_checker_value
        return score_box

    elif score_box[2] == score_box[5] == score_box[8]:
        score_box[2] = score_box[5] = score_box[8] = winner_checker_value
        return score_box

    else:
        return 1


def computer_brain_base(human_input, main_box_status):

    # Attack brain stage
    if main_box_status[0] == main_box_status[1] == filled_list2 and main_box_status[3 - 1][2] == ' ':
        return 3
    elif main_box_status[1] == main_box_status[2] == filled_list2 and main_box_status[1 - 1][2] == ' ':
        return 1
    elif main_box_status[0] == main_box_status[2] == filled_list2 and main_box_status[2 - 1][2] == ' ':
        return 2
    elif main_box_status[3] == main_box_status[4] == filled_list2 and main_box_status[6 - 1][2] == ' ':
        return 6
    elif main_box_status[4] == main_box_status[5] == filled_list2 and main_box_status[4 - 1][2] == ' ':
        return 4
    elif main_box_status[3] == main_box_status[5] == filled_list2 and main_box_status[5 - 1][2] == ' ':
        return 5
    elif main_box_status[6] == main_box_status[7] == filled_list2 and main_box_status[9 - 1][2] == ' ':
        return 9
    elif main_box_status[7] == main_box_status[8] == filled_list2 and main_box_status[7 - 1][2] == ' ':
        return 7
    elif main_box_status[6] == main_box_status[8] == filled_list2 and main_box_status[8 - 1][2] == ' ':
        return 8
    elif main_box_status[0] == main_box_status[3] == filled_list2 and main_box_status[7 - 1][2] == ' ':
        return 7
    elif main_box_status[0] == main_box_status[6] == filled_list2 and main_box_status[4 - 1][2] == ' ':
        return 4
    elif main_box_status[3] == main_box_status[6] == filled_list2 and main_box_status[1 - 1][2] == ' ':
        return 1
    elif main_box_status[1] == main_box_status[4] == filled_list2 and main_box_status[8 - 1][2] == ' ':
        return 8
    elif main_box_status[1] == main_box_status[7] == filled_list2 and main_box_status[5 - 1][2] == ' ':
        return 5
    elif main_box_status[4] == main_box_status[7] == filled_list2 and main_box_status[2 - 1][2] == ' ':
        return 2
    elif main_box_status[2] == main_box_status[8] == filled_list2 and main_box_status[6 - 1][2] == ' ':
        return 6
    elif main_box_status[5] == main_box_status[8] == filled_list2 and main_box_status[3 - 1][2] == ' ':
        return 3
    elif main_box_status[2] == main_box_status[5] == filled_list2 and main_box_status[9 - 1][2] == ' ':
        return 9
    elif main_box_status[0] == main_box_status[4] == filled_list2 and main_box_status[9 - 1][2] == ' ':
        return 9
    elif main_box_status[0] == main_box_status[8] == filled_list2 and main_box_status[5 - 1][2] == ' ':
        return 5
    elif main_box_status[4] == main_box_status[8] == filled_list2 and main_box_status[1 - 1][2] == ' ':
        return 1
    elif main_box_status[2] == main_box_status[4] == filled_list2 and main_box_status[7 - 1][2] == ' ':
        return 7
    elif main_box_status[2] == main_box_status[6] == filled_list2 and main_box_status[5 - 1][2] == ' ':
        return 5
    elif main_box_status[4] == main_box_status[6] == filled_list2 and main_box_status[3 - 1][2] == ' ':
        return 3

    # Defence brain stage
    elif main_box_status[0] == main_box_status[1] == filled_list1 and main_box_status[3 - 1][2] == ' ':
        return 3
    elif main_box_status[1] == main_box_status[2] == filled_list1 and main_box_status[1 - 1][2] == ' ':
        return 1
    elif main_box_status[0] == main_box_status[2] == filled_list1 and main_box_status[2 - 1][2] == ' ':
        return 2
    elif main_box_status[3] == main_box_status[4] == filled_list1 and main_box_status[6 - 1][2] == ' ':
        return 6
    elif main_box_status[4] == main_box_status[5] == filled_list1 and main_box_status[4 - 1][2] == ' ':
        return 4
    elif main_box_status[3] == main_box_status[5] == filled_list1 and main_box_status[5 - 1][2] == ' ':
        return 5
    elif main_box_status[6] == main_box_status[7] == filled_list1 and main_box_status[9 - 1][2] == ' ':
        return 9
    elif main_box_status[7] == main_box_status[8] == filled_list1 and main_box_status[7 - 1][2] == ' ':
        return 7
    elif main_box_status[6] == main_box_status[8] == filled_list1 and main_box_status[8 - 1][2] == ' ':
        return 8
    elif main_box_status[0] == main_box_status[3] == filled_list1 and main_box_status[7 - 1][2] == ' ':
        return 7
    elif main_box_status[0] == main_box_status[6] == filled_list1 and main_box_status[4 - 1][2] == ' ':
        return 4
    elif main_box_status[3] == main_box_status[6] == filled_list1 and main_box_status[1 - 1][2] == ' ':
        return 1
    elif main_box_status[1] == main_box_status[4] == filled_list1 and main_box_status[8 - 1][2] == ' ':
        return 8
    elif main_box_status[1] == main_box_status[7] == filled_list1 and main_box_status[5 - 1][2] == ' ':
        return 5
    elif main_box_status[4] == main_box_status[7] == filled_list1 and main_box_status[2 - 1][2] == ' ':
        return 2
    elif main_box_status[2] == main_box_status[8] == filled_list1 and main_box_status[6 - 1][2] == ' ':
        return 6
    elif main_box_status[5] == main_box_status[8] == filled_list1 and main_box_status[3 - 1][2] == ' ':
        return 3
    elif main_box_status[2] == main_box_status[5] == filled_list1 and main_box_status[9 - 1][2] == ' ':
        return 9
    elif main_box_status[0] == main_box_status[4] == filled_list1 and main_box_status[9 - 1][2] == ' ':
        return 9
    elif main_box_status[0] == main_box_status[8] == filled_list1 and main_box_status[5 - 1][2] == ' ':
        return 5
    elif main_box_status[4] == main_box_status[8] == filled_list1 and main_box_status[1 - 1][2] == ' ':
        return 1
    elif main_box_status[2] == main_box_status[4] == filled_list1 and main_box_status[7 - 1][2] == ' ':
        return 7
    elif main_box_status[2] == main_box_status[6] == filled_list1 and main_box_status[5 - 1][2] == ' ':
        return 5
    elif main_box_status[4] == main_box_status[6] == filled_list1 and main_box_status[3 - 1][2] == ' ':
        return 3

    # No reasoning stage
    else:
        val = human_input
        options = [val + 1, val - 1, val + 2, val - 2, val + 3, val - 3, val + 4, val - 4, val + 5, val - 5, val + 6, val - 6, val + 7, val - 7, val + 8, val - 8]
        valid_options = [x for x in options if 9 >= x >= 0]
        computer_call = random.choice(valid_options)
        if main_box_status[computer_call - 1][2] == ' ':
            return computer_call
        else:
            computer_call = computer_brain_base(human_input, main_box_status)
            return computer_call
