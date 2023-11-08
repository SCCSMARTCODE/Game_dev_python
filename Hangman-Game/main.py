import hangman_function as hang
"""
This is the module that contain the Main function driving Hang_man
"""


def main():
    """This is the main function that runs
            the Hangman Game
                this is pretty Cool and Nice
        Arg:
            None
        Return:
            None
    """

    # Game Starter
    play = 'Y'
    play_round = 0
    play_round_success = None
    play_round_failure = None

    # start up mark
    print("\t\t\tTHIS IS THE HANGMAN GAME DEV @SM@I.COM\n")

    # Game loop rounds
    while play.upper() == 'Y':

        print("\t\t\t\t  Predict The HangMan's Letter\n")

        # Update trackers
        play_round_success = 0
        play_round_failure = 0
        build_hang_man = 0
        guess_this_update = []
        guessed_box_update = []

        # get the word to guess
        guess_this = hang.word_to_guess()

        # load the user sheet with blank spaces
        for x in guess_this:
            guess_this_update.append("_")

        # Display Starts
        while build_hang_man != 9:
            hang.hang_structure(build_hang_man)
            print("\nGuess -->\t", end="")

            for x in guess_this_update:
                print(x.upper(), end=" ")
            print('\n')

            letter_guessed = input("Pick a letter --> ")
            # check if user input is empty or noy
            while len(letter_guessed) == 0:
                letter_guessed = input("Pick a letter --> ")
            # check if user input is not letter
            while not str(letter_guessed).isalpha():
                print("\ninvalid input:")
                letter_guessed = input("Pick a letter not digit or signs\nonly letters are valid options --> ")
            # check if only one letter is passed in
            while len(letter_guessed) > 1:
                print("invalid input:")
                print("\t\tYou can only guess one of the letters.")
                letter_guessed = input("Pick a letter --> ")

            check = hang.guessed_letter_tracker(guessed_box_update, letter_guessed)

            # Avoiding repetition of letters
            while not check:
                letter_guessed = input("Pick a letter --> ")
                check = hang.guessed_letter_tracker(guessed_box_update, letter_guessed)

            # Print the guessed letter collection
            print("Guessed Letters: ", end="")
            for x in guessed_box_update:
                print(x.upper(), end=" ")
            print('\n')

            # check if user input is valid
            letter_guessed_str = str(letter_guessed)
            if letter_guessed_str.upper() in guess_this or letter_guessed_str.lower() in guess_this:
                i = 0
                for x in guess_this:
                    if letter_guessed_str.upper() == x or letter_guessed_str.lower() == x:
                        guess_this_update[i] = letter_guessed
                    i += 1
            # if not valid
            #       then start constructing HANGMAN
            else:
                build_hang_man += 1

            # check failure
            if build_hang_man == 9:
                hang.hang_structure(build_hang_man)
                print('\t\t[', end='')
                for x in guess_this_update:
                    print(x.upper(), end="")
                print(']\t-->\t\t[{}]\n'.format(guess_this.upper()))
                play_round += 1
                play_round_failure += 1
                print("So sorry, You struck out.")
                play = input("Do you want to play again ? Y/N: ")
                print("")
                continue

            # check success
            if '_' not in guess_this_update:
                play_round += 1
                play_round_success += 1
                print("Guess -->\t" + guess_this.upper())
                print("YOU WIN")
                play = input("Do you want to play again ? Y/N: ")
                print("")
                break

    # End of Game print out for evaluation
    else:
        print("\t\tPerformance Details !!!-:")
        print("\t\t\t\tNumber of Games played in total #_ {} _#".format(play_round))
        print("\t\t\t\tNumber of successfully dashed words #_ {} _#".format(play_round_success))
        print("\t\t\t\tNumber of lost words #_ {} _#".format(play_round_failure))
        print("\t\t\t\tThanks for playing...")


# Run main() if this module is executed
if __name__ == '__main__':
    main()
