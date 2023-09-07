import random
import sys

CHOICES = ['🔴', '🟠', '🟡', '🟢', '🔵', '🟣']

def main():
    game = True
    count = 0
    
    print(introduction())
    code = set_code()
    
    while game == True:
        try:
            count += 1
            guess = input('Input your guess here: ').strip()
            print(check_code(code, guess))
            if guess == code:
                count = 0
                print(win_message())
                game = False
            if count == 10:
                sys.exit(lose_message())
            for i in guess:
                if not i in CHOICES:
                    raise ValueError
        except ValueError:
            count -= 1
            print('Enter a valid code with the colors from the choices')
            pass
    
    


# Computer sets the code the user has to guess
def set_code():
    code = ''
    for _ in range(4):
        code += random.choice(CHOICES)
    return code

def check_code(code, guess):
    black = 0
    white = 0
    for c, g in zip(code, guess):
            if c == g:
                black += 1
                white -= 1
    for g in guess:
        if g in code:
            white += 1
            
    return f'You have {black} colors that are in the code and are in the right position.\nYou have {white} colors that are in the code but are in the wrong position.'
        



def introduction():
    return 'Welcome to Mastermind!\nAs the codemaker, the computer will set a random code made up of four different colors.\nThe colors to choose from are: "🔴", "🟠", "🟡", "🟢", "🔵", and "🟣"\nAs the codebreaker, you must try to break the code!\nComputer will provide hints after every guess.\nGuess the code within 10 tries to become the mastermind'

def win_message():
    return 'You managed to break the code! You are the mastermind!'

def lose_message():
    return 'You have lost to the codemaker :('


if __name__ == '__main__':
    main()