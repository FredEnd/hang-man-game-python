from word_gen import Wlist
from RandomWordGenerator import RandomWord
import pyfiglet


# this subroutine selects the game mode of hangman txt is recommended
def gamem(x):
    if x == "txt":
        return Wlist()
    elif x == "ran":
        y = RandomWord()
        return y.generate()
    else:
        gamemr = str(input("invalid input please try again 'txt' or 'ran'\n"))
        return gamem(gamemr)


# this subroutine turns the generated word into a set of underscores
def word_(a):
    display = ""
    for words in a:
        display = display + "_"
    return display


# this subroutine uses the import pyfiglet to enlarge the display output
def font_dis(s):
    re = pyfiglet.figlet_format(s)
    return re


# this subroutine filters the guess so that the user only inputs one word
def one_word(imp):
    implen = len(imp)
    if implen > 1 or implen < 0:
        print("guess invalid only one letter")
    elif imp != str(imp):
        print("invalid data type please type a string letter e.g 'a','b','c' as your guess")
    else:
        return imp.lower()


# this subroutine finds the guess in the word and then changes the output for the display to show the guessed word
def main_hang(guess, o, w):
    indexes = []
    new = ""
    for i in range(len(w)):
        if w[i] == guess:
            indexes.append(i)
            status = True
    print(indexes)
    for j in range(len(o)):
        if j in indexes:
            new += guess
        else:
            if o[j] != "_":
                new += o[j]
            else:
                new += "_"
    return new

# this subroutine decides when the code ends when you have solved the hang man problem
def end_check(output_end):
    print(output_end)
    for letters in output_end:
        if letters == "_":
            return False
    print("you have guessed the word")
    return True

# this subroutine is the start where inputs are taken and functions are decided
def game_loop():
    gamemr = str(input("please enter the game mode you want to play 'txt' or 'ran' i reconmend not doing txt\n"))
    wordout = gamem(gamemr)
    output = word_(wordout)
    print(wordout)
    gameloop = True
    while gameloop == True:
        guess = str(input("please type your first guess\n"))
        guess = one_word(guess)
        newout = main_hang(guess, output, wordout)
        output = newout
        end = end_check(output)
        if end == True:
            gameloop = False
        print(font_dis(output))

# this restarts the code
restart = str(input("do you want to play hang man Y or N")).upper()
if restart == "Y":
    game_loop()
elif restart == "N":
    exit()
else:
    print("invalid input")
    restart = str(input("do you want to play hang man Y or N")).upper()
