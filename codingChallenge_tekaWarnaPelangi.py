#!/usr/bin/env python

import random

def main():
    #memulakan permainan
    """Start the rainbow colour guessing game."""
    print("Guess the rainbow colour?")
    
    #pilihan warna 
    colour = [
        "red",
        "orange",
        "yellow",
        "green",
        "blue",
        "indigo",
        "violet"
        ]

    x =random.choice(colour)
    max_trials= 3
    trial=0
    guess = None
    #print(x)
    while trial<max_trials:
        guess = str(input("What colour are we thinking of? "))
        
        if x == guess:
            print(f"You guessed.Congratulations you got it right!".format(guess))
            break
        else:
            print(f"Unfortunately you got the wrong answer.".format(guess))
            print(f"You have {max_trials} chances remaining.")
            max_trials -= 1
        if max_trials == 0:
            print(f"out of attempts. The colour is actually {x}.".format(guess))
        
main()