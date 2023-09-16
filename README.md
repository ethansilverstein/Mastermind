# Mastermind
#### Video Demo:  https://youtu.be/yhVYQOtav3I
#### Description:

This project is based on the board game Mastermind. The board game plays like this: The codemaker makes a code made up of 4 colors while the other player isn't looking. Then, the codebreaker tries to break the code by guessing combinations of the code. The codemaker then puts certain hints for the codebreaker. If there is a color that is in the code the codemaker made and is in the right position, then the codemaker puts a black peg in the slot, if a color is in the code but in the wrong spot, then the codemaker places a white peg in the slot. The codebreaker tries to use these hints to guess the code within 10 tries. If the codebreaker breaks the code within those tries, then they are the mastermind!
    
In this version of the game, the computer is the codemaker and it sets up a 4 color code using letters to represent the colors. Those colors are Red (R), Orange (O), Yellow (Y), Green (G), Blue (B), and Purple (P). The user is the codebreaker and the user tries to guess the code using the letters. After that, the computer outputs hints like in the original board game. The user gets 10 tries to fully guess the whole code and become the Mastermind. Any invalid codes do not count towards the 10 tries and it reprompts the user to input a valid code.

#### Explanation of files:

.gitignore: I made this file to make sure that I don't upload any files that I don't want on the repo like \__pycache__ or .pytest_cache

project.py: The main file of my project. Contains all the main logic of the project.

README.md: The file right here, an explanation of my project and how it works.

test_project.py: This file contains the tests for the functions in my main file, project.py
