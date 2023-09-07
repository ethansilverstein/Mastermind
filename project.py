import random
import sys

CHOICES = ['🔴', '🟠', '🟡', '🟢', '🔵', '🟣' ]

def main():
    print(introduction())
    code = set_code()
    for v in range(10):
        guess = input('Input your guess here: ')
        if guess == code:
            print(win_message())
            sys.exit(0)
    print(lose_message())
    
    


# Computer sets the code the user has to guess
def set_code():
    code = ''
    for _ in range(4):
        code += random.choice(CHOICES)
    return code

def check_code():
    ...



def introduction():
    return 'Welcome to Mastermind!\nAs the codemaker, the computer will set a random code made up of four different colors.\nAs the codebreaker, you must try to break the code!\nComputer will provide hints after every guess.\nGuess the code within 10 tries to become the mastermind'

def win_message():
    return 'You managed to break the code! You are the mastermind!'

def lose_message():
    return 'Codemaker'


if __name__ == '__main__':
    main()