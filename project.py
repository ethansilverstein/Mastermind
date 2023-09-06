import random

CHOICES = ['🔴', '🟠', '🟡', '🟢', '🔵', '🟣' ]

def main():
    code = set_code()


# Computer sets the code the user has to guess
def set_code():
    code = ''
    for v in range(4):
        code += random.choice(CHOICES)
    return code


if __name__ == '__main__':
    main()