#!/usr/bin/env python

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4,
         "y": 4, "x": 8, "z": 10}


def scrabble_score(word):
    total = 0
    word = word.lower()
    for char in word:
        letter_score = score[char]
        total = total + letter_score
        # print(char, letter_score)  # for debug purposes
    return str(total)


while True:
    print("Welcome to Scrabble Scores. \nThe program that shows you the scores on the tiles!")
    print("What would you like to do today?\n [1] Find the score for a word \n [2] Compare scores of two words\n")
    menu_choice = input("Please choose 1 or 2: ")
    if menu_choice != "1" or "2":
        input("Choice invalid. Please select 1 or 2:")
    elif menu_choice == "1":
        user_word = input("What is your word?: ")
        print("The scrabble score for {} is: {}".format(user_word, (scrabble_score(user_word))))
        quit_choice = input("Would you like to check another word? y/n ")
        if quit_choice == "n":
            break
    else:
        print("What two words would you like to compare today?")
        word_1 = input("Word 1: ")
        word_2 = input("Word 2: ")
        score_word_1 = scrabble_score(word_1)
        score_word_2 = scrabble_score(word_2)
        print("{} will score {}".format(word_1, score_word_1))
        print("{} will score {}".format(word_2, score_word_2))
        quit_choice = input("Would you like to check another word? y/n ")
        if quit_choice == "n":
            break
