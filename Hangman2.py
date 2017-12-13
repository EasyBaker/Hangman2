#Hangman
#By Nathan Blouse
import os
import random
import math

name = input("What is your name?")
game_start = True
while game_start:
    answer = input("Would you like to play the normal version where you guess the word or where somebody else enters the word for you " + name + "? Enter 'normal' or 'self'.")
    if str.lower(answer) == "normal":
        game_work = True
        while game_work:
            def get_puzzle():
                path = "Puzzles"
                
                file_names = os.listdir(path)
                
                for i, f in enumerate(file_names):
                    this_file = f
                    with open(path + "/" + this_file, 'r') as f:
                        beginning_lines = f.read().splitlines()
                    category_name = beginning_lines[0]
                    print(str(i + 1) + ") " + category_name)

                choice = input('pick one: ')
                choice = int(choice)

                file = path + "/" + file_names[choice - 1]

                with open(file, 'r') as f:
                    lines = f.read().splitlines()
                this_one_beginning = lines[0]
                print(this_one_beginning)
                
                word = random.choice( lines[1:] )
                return str.lower(word)
            
            def get_solved(puzzle, guesses):
                solved = ""

                for letter in puzzle:
                    if letter in guesses:
                        solved += letter
                    elif letter == " ":
                        solved += " "
                    else:
                        solved += "-"

                return solved

            def get_guess():
                while True:
                    letter = input("Guess a letter " + name + ": ")

                    if len(letter) == 1:
                        return letter
                    else:
                        print("I don't understand " + name + ". Please enter 1 character.")

            def display_board(solved, strikes, correct_guesses, incorrect_guesses):
                print(solved)
                print("Strikes: " + str(strikes))
                print("Correct Guesses: " + str(correct_guesses))
                print("Incorrect Guesses: " + str(incorrect_guesses))

            def beginning_splash_screen():
                with open("Art/drunk_mickey.txt", 'r') as f:
                    lines = f.read().splitlines()
                for i, f in enumerate(lines):
                    print(f)

            def end_splash_screen():
                print("*************")
                print("*****Bye*****")
                print("*****See*****")
                print("*****YOU*****")
                print("**NEXT TIME**")
                print("*************")
                print("BY: NATHAN BLOUSE")
                print("COMPLETED: NOVEMBER 9")
                
            def display_man(strikes):
                if strikes == 0:
                    with open("Art/0_strikes.txt", 'r') as f:
                        lines = f.read().splitlines()
                    for i, f in enumerate(lines):
                        print(f)
                    
                elif strikes == 1:
                    with open("Art/1_strike.txt", 'r') as f:
                        lines = f.read().splitlines()
                    for i, f in enumerate(lines):
                        print(f)
                    
                elif strikes == 2:
                    with open("Art/2_strikes.txt", 'r') as f:
                        lines = f.read().splitlines()
                    for i, f in enumerate(lines):
                        print(f)
                    
                elif strikes == 3:
                    with open("Art/3_strikes.txt", 'r') as f:
                        lines = f.read().splitlines()
                    for i, f in enumerate(lines):
                        print(f)
                    
                elif strikes == 4:
                    with open("Art/4_strikes.txt", 'r') as f:
                        lines = f.read().splitlines()
                    for i, f in enumerate(lines):
                        print(f)
                    
                elif strikes == 5:
                    with open("Art/5_strikes.txt", 'r') as f:
                        lines = f.read().splitlines()
                    for i, f in enumerate(lines):
                        print(f)
                    
                else:
                    with open("Art/6_strikes.txt", 'r') as f:
                        lines = f.read().splitlines()
                    for i, f in enumerate(lines):
                        print(f)
                              
            def show_result(strikes):
                if strikes < limit:
                    print("You Win " + name + "!")
                else:
                    print("You lose... Better luck next time " + name + "!")

            def show_credits():
                print("Thanks for playing " + name + "! I'll see you next time!")

            def play_again():
                while True:
                    decision = input("Would you like to play again " + name + "? (y/n) ")

                    if decision == 'y' or decision == 'yes':
                        return True
                    elif decision == 'n' or decision == 'no':
                        return False
                    else:
                        print("I don't understand " + name + ". Please enter 'y' or 'n'.")
                        
            def play(strikes, limit):
                puzzle = get_puzzle()
                guesses = ""
                correct_guesses = ""
                incorrect_guesses = ""
                solved = get_solved(puzzle, guesses)

                print(solved)

                while solved != puzzle:
                    letter = get_guess()

                    if letter not in puzzle:
                        strikes += 1
                        incorrect_guesses += letter
                        if strikes == limit + 1:
                            break
                    else:
                        correct_guesses += letter
                    
                    guesses += letter
                    solved = get_solved(puzzle, guesses)
                    display_man(strikes)
                    display_board(solved, strikes, correct_guesses, incorrect_guesses)

                show_result(strikes)
            beginning_splash_screen()

            strikes = 0
            limit = 6
                
            playing = True

            while playing:
                print("You have " + str(limit) + " tries.")
                play(strikes, limit)
                playing = play_again()

            end_splash_screen()
            show_credits()
            game_start = False
            game_work = False
    elif str.lower(answer) == "self":
        game_work = True
        while game_work:
            def get_puzzle():
                word = input("Please get somebody to enter a word that they would like you to guess " + name + ". Turn your head away as they do so.... ")
                return word
            def get_solved(puzzle, guesses):
                solved = ""

                for letter in puzzle:
                    if letter in guesses:
                        solved += letter
                    elif letter == " ":
                        solved += " "
                    else:
                        solved += "-"

                return solved

            def get_guess():
                while True:
                    letter = input("Guess a letter " + name + ": ")

                    if len(letter) == 1:
                        return letter
                    else:
                        print("I don't understand " + name + ". Please enter 1 character.")

            def display_board(solved, strikes, correct_guesses, incorrect_guesses):
                print(solved)
                print("Strikes: " + str(strikes))
                print("Correct Guesses: " + str(correct_guesses))
                print("Incorrect Guesses: " + str(incorrect_guesses))

            def beginning_splash_screen():
                print("*************")
                print("***WELCOME***")
                print("*****TO*****")
                print("***HANGMAN***")
                print("*************")

            def end_splash_screen():
                print("*************")
                print("*****Bye*****")
                print("*****See*****")
                print("*****YOU*****")
                print("**NEXT TIME**")
                print("*************")
                print("BY: NATHAN BLOUSE")
                print("COMPLETED: NOVEMBER 9")
                
            def display_man(strikes):
                if strikes == 0:
                    with open("Art/0_strikes.txt", 'r') as f:
                        lines = f.read().splitlines()
                    for i, f in enumerate(lines):
                        print(f)
    
                elif strikes == 1:
                    with open("Art/1_strikes.txt", 'r') as f:
                        lines = f.read().splitlines()
                    for i, f in enumerate(lines):
                        print(f)
                    
                elif strikes == 2:
                    with open("Art/2_strikes.txt", 'r') as f:
                        lines = f.read().splitlines()
                    for i, f in enumerate(lines):
                        print(f)
                    
                elif strikes == 3:
                    with open("Art/3_strikes.txt", 'r') as f:
                        lines = f.read().splitlines()
                    for i, f in enumerate(lines):
                        print(f)
                elif strikes == 4:
                    with open("Art/4_strikes.txt", 'r') as f:
                        lines = f.read().splitlines()
                    for i, f in enumerate(lines):
                        print(f)
                    
                elif strikes == 5:
                    with open("Art/5_strikes.txt", 'r') as f:
                        lines = f.read().splitlines()
                    for i, f in enumerate(lines):
                        print(f)
                    
                else:
                    with open("Art/6_strikes.txt", 'r') as f:
                        lines = f.read().splitlines()
                    for i, f in enumerate(lines):
                        print(f)
                          
            def show_result(strikes):
                if strikes < limit + 1:
                    print("You Win " + name + "!")
                else:
                    print("You lose... Better luck next time " + name + "!")

            def show_credits():
                print("Thanks for playing " + name + "! I'll see you next time!")

            def play_again():
                while True:
                    decision = input("Would you like to play again " + name + "? (y/n) ")

                    if decision == 'y' or decision == 'yes':
                        return True
                    elif decision == 'n' or decision == 'no':
                        return False
                    else:
                        print("I don't understand " + name + ". Please enter 'y' or 'n'.")
                        
            def play(strikes, limit):
                puzzle = get_puzzle()
                for i in range(40):
                    print("")
                beginning_splash_screen()
                print("You have " + str(limit) + " tries.")
                guesses = ""
                correct_guesses = ""
                incorrect_guesses = ""
                solved = get_solved(puzzle, guesses)

                print(solved)

                while solved != puzzle:
                    letter = get_guess()

                    if letter not in puzzle:
                        strikes += 1
                        incorrect_guesses += letter
                        if strikes == limit + 1:
                            break
                    else:
                        correct_guesses += letter
                    
                    guesses += letter
                    solved = get_solved(puzzle, guesses)
                    display_man(strikes)
                    display_board(solved, strikes, correct_guesses, incorrect_guesses)

                show_result(strikes)
            
            strikes = 0
            limit = 6
                
            playing = True

            while playing:
                play(strikes, limit)
                playing = play_again()

            end_splash_screen()
            show_credits()
            game_start = False
            game_work = False
    else:
        print("I don't understand. Please enter 'normal' or self' " + name + ".")

