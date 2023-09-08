import random
import sys

CHOICES = ['R', 'O', 'Y', 'G', 'B', 'P']

def main():
    game = True
    count = 0
    
    print(introduction())
    code = set_code()
    code = 'RRYY'
    while game:
        try:
            count += 1
            guess = input('Input your guess here: ').strip()
            if guess == code:
                count = 0
                print(win_message())
                game = False
                break
            if count == 10:
                sys.exit(lose_message())
            for i in guess:
                if not i in CHOICES:
                    raise ValueError
            print(check_code(code, guess))
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
    checked = []
    black = 0
    white = 0
    for c, g in zip(code, guess):
        if g == c:
            black += 1
            checked.append(g)
    for g in guess:
        if g in code and g not in checked:
            white += 1
                
    return f'You have {black} colors that are in the code and are in the right position.\nYou have {white} colors that are in the code but are in the wrong position.'
        



def introduction():
    return 'Welcome to Mastermind!\nAs the codemaker, the computer will set a random code made up of four different colors.\nThe colors to choose from are: "🔴 (R)", "🟠 (O)", "🟡 (Y)", "🟢 (G)", "🔵 (B)", and "🟣 (P)"\nEnter the letters, not the emojis\nAs the codebreaker, you must try to break the code!\nComputer will provide hints after every guess.\nGuess the code within 10 tries to become the mastermind'

def win_message():
    return 'You managed to break the code! You are the mastermind!'

def lose_message():
    return 'You have lost to the codemaker :('


if __name__ == '__main__':
    main()