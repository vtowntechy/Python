print """
A classic game of rock paper scissors. You'll play against the computer.
 
The rules are:
> Rock breaks scissor
> Scissor cuts paper
> Paper covers rock
 
You can play any number of times you want.
The result will be the sum of the total number of wins by a player.
If you win the most number of times, you are the winner!"""
 
import random
comp_dict = {"r":"Rock", "p":"Paper", "s":"Scissor"}
repeat = int(raw_input("\nHow many times will you like to play?: "))
 
def play():
    h = raw_input("\nPlease make a choice - r for Rock, p for paper, s for scissor: ")
    print "\nYou chose", comp_dict.get(h)
    c = random.choice(comp_dict.keys())
    print "Computer chose", comp_dict.get(c) ,"\n"
    global win
    global lose
    global draw
     
    if (h == c):
        print "Draw!"
        draw = draw + 1
    elif (h == "p" and c == "r"):
        print "You win"
        win = win + 1
    elif (h == "r" and c == "p"):
        print "Computer wins"
        lose = lose + 1
    elif (h == "r" and c == "s"):
        print "You win"
        win = win + 1
    elif (h == "s" and c == "r"):
        print "Computer wins"
        lose = lose + 1
    elif (h == "s" and c == "p"):
        print "You win"
        win = 
