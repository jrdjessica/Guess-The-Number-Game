"""A number-guessing game."""

import random

# Put your code here
best_score = None
play = True
print('Sup. What\'s your name player?')
player_name = input('(type in your name) ')
print('Do you want to guess a number or do you want the computer to guess?')
choice = input(
    '(type "me" if you want to guess or type "comp" if you want the computer to guess) ')

if choice == 'me':

    while play == True:
        print('It\'s up to you to choose the range.')
        lower_limit = int(input('(type the lower limit) '))
        upper_limit = int(input('(type the upper limit) '))

        print(
            f'{player_name}, I\'m thinking of a number between {lower_limit} and {upper_limit}.')
        print('Try to guess my number.')

        num = random.randint(lower_limit, upper_limit)
        count = 0

        while True:
            guess = int(input('Your guess? '))
            if type(guess) == int and guess >= lower_limit and guess <= upper_limit:
                count += 1
                if guess > num:
                    print('Your guess is too high. Try again.')
                elif guess < num:
                    print('Your guess is too low. Try again.')
                else:
                    print(
                        f'Well done {player_name}. You found my number in {count} tries.')
                    if best_score == None or count < best_score:
                        best_score = count
                        print('You just received your best score. Congrats!!')
                    break

            else:
                print(
                    "Hey numbnuts, that's not a valid integer. What are you, a toddler? Try again.")

            if count == 10:
                print('You took too many tries. You loser.')
                break

        print(f'Your current best score is {best_score}.')
        print("Do you want to play again?")
        play_again = input("(y/n) ")
        if play_again == "y":
            pass
        elif play_again == "n":
            play = False
        else:
            print('Not a valid input. You don\'t get to play anymore. Boo Hoo.')
            play = False

elif choice == 'comp':

    while play == True:
        print('Choose lower and upper limits for the guessing range.')
        start = int(input('(type lower limit) '))
        end = int(input('(type upper limit) '))
        print(f'Choose a number between {start} and {end}.')

        while True:
            comp_guess = random.randint(start, end)
            print(f'Is {comp_guess} too high, too low, or correct?')
            player_response = input(
                '(type "too high", "too low", or "correct") ')
            if player_response == 'too high':
                end = comp_guess - 1
            elif player_response == 'too low':
                start = comp_guess + 1
            elif player_response == 'correct':
                print('The computer wins. Your number is stupid like your face.')
                break
            else:
                print('Invalid. Can you even read bro? Game over.')
                break

        print("Do you want to play again?")
        play_again = input("(y/n) ")
        if play_again == "y":
            pass
        elif play_again == "n":
            play = False
        else:
            print('Not a valid input. You don\'t get to play anymore. Boo Hoo.')
            play = False

else:
    print('You stupid. You don\'t get to play anymore.')
