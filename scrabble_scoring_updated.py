#!/usr/bin/env python
"""
Created by Jiggs

Scrabble scoring tool to calculate the score of a given word.
Can also compare the scores of any 2 given words.
"""

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, "r": 1, "u": 1, "t": 1, "w": 4, "v": 4,
         "y": 4, "x": 8, "z": 10}


def scrabble_score(word):
    total = 0
    word = word.lower()
    for char in word:
        letter_score = score[char]
        total = total + letter_score  # print(char, letter_score)  # for debug purposes
    return str(total)


def prog_exit():
    global run
    exit_option = input("Would you like to check another word? y/n ").lower()
    while True:
        if exit_option == "n":
            run = False
            break
        elif exit_option == "y":
            run = True
            break
        else:
            exit_option = input("Would you like to check another word? y/n ").lower()


print("Welcome to Scrabble Scores. \nThe program that shows you the scores on the tiles!")

run = True
while run:
    print("\nWhat would you like to do today?\n [1] Find the score for a word \n [2] Compare scores of two words\n")
    menu_choice = input("Please choose 1 or 2: ")
    # print(menu_choice, type(menu_choice))
    if menu_choice == "1" or "2":
        if menu_choice == "1":
            user_word = input("\nWhat is your word?: ")
            print("The scrabble score for {} is: {}".format(user_word, (scrabble_score(user_word))))
            prog_exit()
        elif menu_choice == "2":
            print("\nWhat two words would you like to compare today?")
            word_1 = input("Word 1: ")
            word_2 = input("Word 2: ")
            score_word_1 = scrabble_score(word_1)
            score_word_2 = scrabble_score(word_2)
            print("{} will score {}".format(word_1, score_word_1))
            print("{} will score {}".format(word_2, score_word_2))
            prog_exit()
