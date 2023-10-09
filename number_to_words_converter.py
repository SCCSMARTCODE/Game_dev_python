def unit(val):
    u_output = num_identifier1(val)
    return u_output


def tens(val):
    t_output = num_identifier2(val)
    return t_output


def hundred(val):
    h_output = num_identifier1(val)
    return h_output


def num_identifier1(val):
    if val == 0:
        return "Zero"
    elif val == 1:
        return "One"
    elif val == 2:
        return "two"
    elif val == 3:
        return "three"
    elif val == 4:
        return "four"
    elif val == 5:
        return "five"
    elif val == 6:
        return "six"
    elif val == 7:
        return "seven"
    elif val == 8:
        return "eight"
    elif val == 9:
        return "nine"
    else:
        return "Invalid input"


def num_identifier2(val):
    if val == 0:
        return "Zero"
    elif val == 2:
        return "twenty"
    elif val == 3:
        return "thirty"
    elif val == 4:
        return "forty"
    elif val == 5:
        return "fifty"
    elif val == 6:
        return "sixty"
    elif val == 7:
        return "seventy"
    elif val == 8:
        return "eighty"
    elif val == 9:
        return "ninty"
    else:
        return "Invalid input"


def num_identifier2i(val):
    if val == 0:
        return "Ten"
    elif val == 1:
        return "Eleven"
    elif val == 2:
        return "Twelve"
    elif val == 3:
        return "Thirteen"
    elif val == 4:
        return "fourteen"
    elif val == 5:
        return "fifteen"
    elif val == 6:
        return "sixteen"
    elif val == 7:
        return "seventeen"
    elif val == 8:
        return "eighteen"
    elif val == 9:
        return "nineteen"
    else:
        return ""


def hundred_check(user_number):
    if len(user_number) == 3:
        u_out0 = hundred(int(user_number[0]))
        u_out1 = tens(int(user_number[1]))
        u_out2 = unit(int(user_number[2]))

        # printer line start
        # bugs home
        # issues still dey here
        if '0' not in user_number:
            if user_number[1] == '1':
                u_out2i = num_identifier2i(int(user_number[2]))
                return "{} hundred and {}".format(u_out0, u_out2i)
            else:
                return "{} hundred and {} {}".format(u_out0, u_out1, u_out2)
        elif user_number[0] == user_number[1] == user_number[2] == '0':
            return "{}".format(u_out2)
        elif user_number[0] == user_number[1] == '0':
            return "{}".format(u_out2)
        elif user_number[0] == user_number[2] == '0':
            if user_number[1] == '1':
                u_out2 = num_identifier2i(int(user_number[2]))
                return "{}".format(u_out2)
            else:
                return "{}".format(u_out1)
            # bugs
        elif user_number[1] == user_number[2] == '0':
            return "{} hundred".format(u_out0)
        elif user_number[0] == '0':
            if user_number[1] == '1':
                u_out2 = num_identifier2i(int(user_number[2]))
                return "{}".format(u_out2)
                # bug
            else:
                return "{} {}".format(u_out1, u_out2)
        elif user_number[1] == '0':
            return "{} hundred and {}".format(u_out0, u_out2)
        elif user_number[2] == '0':
            if user_number[1] == '1':
                u_out2 = num_identifier2i(int(user_number[2]))
                return "{} hundred and {}".format(u_out0, u_out2)
            else:
                return "{} hundred and {}".format(u_out0, u_out1)


def tens_check(user_number):
    if len(user_number) == 2:
        if user_number[0] == '1':
            u_out = num_identifier2i(int(user_number[1]))
            return "{}".format(u_out)

        elif user_number[0] == '0':
            u_out2 = unit(int(user_number[1]))
            return "{}".format(u_out2)

        elif user_number[0] != '1' and user_number[0] != '0':
            if user_number[1] != '0':
                u_out1 = tens(int(user_number[0]))
                u_out2 = unit(int(user_number[1]))
                return "{} {}".format(u_out1, u_out2)
            else:
                u_out1 = tens(int(user_number[0]))
                return "{}".format(u_out1)

        else:
            pass


def unit_check(user_number):
    if len(user_number) == 1:
        u_out1 = unit(int(user_number[0]))
        return "{}".format(u_out1)


def print_in_million(user_input_m, _result1, _result2, _result3):
    if user_input_m != "@#$%^&*(":
        if _result1 == 'Zero' and _result2 == 'Zero':
            result_m = "{} in words is --[{}]--".format(user_input_m, _result3)
            # print("here0")
        elif _result1 == _result3 == 'Zero':
            # print("here1")
            result_m = "{} in words is --[{} thousand]--".format(user_input_m, _result2)
        elif _result2 == _result3 == 'Zero':
            # print("here2")
            result_m = "{} in words is --[{} million]--".format(user_input_m, _result1)
        elif _result1 == 'Zero':
            result_m = "{} in words is --[{} thousand, {}]--".format(user_input_m, _result2, _result3)
            # print("here3")
        elif _result2 == 'Zero':
            result_m = "{} in words is --[{} million, {}]--".format(user_input_m, _result1, _result3)
            # print("here4")
        elif _result3 == 'Zero':
            result_m = "{} in words is --[{} million, {} thousand]--".format(user_input_m, _result1, _result2)
            # print("here5")
        else:
            result_m = "{} in words is --[{} million, {} thousand, {}]--".format(user_input_m, _result1, _result2, _result3)
            # print("here6")
        return result_m


print("Welcome to S@mi software @SCCSMARTCODE")
print("\t\t\t\t----------I convert numbers to words-----------")
print("Input --[End]-- to exit")

while 1:
    print("input your number")
    user_input = input()
    if user_input.lower() == "end":
        break
    num_len = len(user_input)
    assess = 1

    for x in user_input:
        w = x
        if w in "+-0123456789":
            assess *= 1
        else:
            assess *= 0
    if assess == 0:
        print("Invalid input\n")
        continue
    if user_input[0] == '-':
        user_input = user_input.replace('-', '')
        print("\nNegative number???")
    elif user_input[0] == '+':
        user_input = user_input.replace('+', '')
        print("\nPositive number???")

    if 7 <= len(user_input) <= 9:
        if len(user_input) == 7:
            result1 = unit_check(user_input[0])
            result2 = hundred_check(user_input[1:4])
            result3 = hundred_check(user_input[4:])
        elif len(user_input) == 8:
            result1 = tens_check(user_input[0:2])
            result2 = hundred_check(user_input[2:5])
            result3 = hundred_check(user_input[5:])
        elif len(user_input) == 9:
            result1 = str(hundred_check(user_input[0:3]))
            result2 = hundred_check(user_input[3:6])
            result3 = hundred_check(user_input[6:])
        else:
            result1 = "--------"
            result2 = "--------"
            result3 = "--------"

        result = print_in_million(user_input, result1, result2, result3)

    elif len(user_input) == 6:
        u_inp1 = user_input[0:3]
        result1 = hundred_check(u_inp1)
        result2 = hundred_check(user_input[3:])
        if result1 == 'Zero':
            result = "{} in words is --[{}]--".format(user_input, result2)
        elif result2 == 'Zero':
            result = "{} in words is --[{} thousand]--".format(user_input, result1)
        else:
            result = "{} in words is --[{} thousand, {}]--".format(user_input, result1, result2)

    elif len(user_input) == 5:
        u_inp1 = user_input[0:2]
        result1 = tens_check(u_inp1)
        result2 = hundred_check(user_input[2:])
        if result1 == 'Zero':
            result = "{} in words is --[{}]--".format(user_input, result2)
        elif result2 == 'Zero':
            result = "{} in words is --[{} thousand]--".format(user_input, result1)
        else:
            result = "{} in words is --[{} thousand, {}]--".format(user_input, result1, result2)

    elif len(user_input) == 4:
        u_inp1 = user_input[0]
        result1 = unit_check(u_inp1)
        result2 = hundred_check(user_input[1:4])
        if result1 == 'Zero':
            result = "{} in words is --[{}]--".format(user_input, result2)
        elif result2 == 'Zero':
            result = "{} in words is --[{} thousand]--".format(user_input, result1)
        else:
            result = "{} in words is --[{} thousand, {}]--".format(user_input, result1, result2)

    elif len(user_input) == 3:
        result = hundred_check(user_input)
        result = "{} in words is --[{}]--".format(user_input, result)
    elif len(user_input) == 2:
        result = tens_check(user_input)
        result = "{} in words is --[{}]--".format(user_input, result)
    elif len(user_input) == 1:
        result = unit_check(user_input)
        result = "{} in words is --[{}]--".format(user_input, result)
    else:
        result = "Sorry\n@sm@i is still working on it"

    print(result)

print("\t\t\t\t\t---------------------------->>>>>>>>>>Thank you @SCCSMARTCODE@SM@I.com<<<<<<<<<<----------------------------")
