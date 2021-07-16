import random
import os
import sys
from time import sleep

def rps():
    options = ["Rock", "Paper", "Scissors"]

    AI = random.choice(options)

    user = input("Pick Rock, Paper, or Scissors: ")
    user = user.lower()

    if user == 'rock' or 'paper' or 'scissors':
        print("The computer chose %s while you chose %s" % (AI, user))

    if user == 'rock':
        if AI == 'Rocsk':
            print('tie game')
        elif AI == 'Paper':
            print("You lose")
        else:
            print("You win")

rps()
sleep(3)
    
if __name__ == '__main__':
    rps()
    os.execv(_file_, sys.argv)
