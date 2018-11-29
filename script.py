from termcolor import colored # https://pypi.org/project/termcolor/
import random

# Shift Player
def player(i):
    if(i == "O"):
        return "X"
    else:
        return "O"
# check who won
def check_win(ma, pl):
    if ma[0] == pl and ma[1] == pl and ma[2] == pl:
       # print("1 " + ma[0] + " " + ma[1] + " " + ma[2])
        return True
    elif ma[3] == pl and ma[4] == pl and ma[5] == pl:
        return True
    elif ma[6] == pl and ma[7] == pl and ma[8] == pl:
        return True
    elif ma[0] == pl and ma[4] == pl and ma[8] == pl:
        return True
    elif ma[2] == pl and ma[4] == pl and ma[6] == pl:
        return True
    elif ma[1] == pl and ma[4] == pl and ma[7] == pl:
        return True
    return False

# Random move from computer
def choiseOfComputer():
    return random.randint(1,9)

def print_matrix():
    print("===========")
    k = 0
    while k < 9:      
        j = 0
        while j < 2:
            print(" "+ matrix[k+j] + " |", end="")
            j = j+1
        print(" " + matrix[k+j] + " ")
        j = 0    
        k = k+3
        #end while
    # end while
    print("===========")
    k = 0

matrix = [" "]*9
sign = "X" 
i = ""

while i != "N".lower():  
    
    print_matrix()

    x = int(input(sign + " Where do you want to place your piece?"))
    matrix[int(x)-1] = sign
    if(check_win(matrix, sign)):
        print(colored(sign + " you win", "red", "on_yellow"))
        print_matrix()
        break
    
    sign = player(sign)

    x = choiseOfComputer()
    matrix[int(x)-1] = sign
    if(check_win(matrix, sign)):
        print(colored(sign + " you win", "red", "on_yellow"))
        print_matrix()
        break

    sign = player(sign)

# end while

