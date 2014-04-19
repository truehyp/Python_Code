import simplegui
import random
import math

num_range = 100
def new_game():
    global num, remain_guess
    num = random.randrange(num_range)
    remain_guess = 7
    print "Number of remaining guess is", remain_guess
    
def range100():
    num_range = 100
    print "Range is [0, 100]"
    new_game()
    
def range1000():
    num_range = 1000
    print "Range is [0, 1000]"
    new_game()
    
def get_input(guess):
    global num, remain_guess
    if (int(guess) == num):
        print "corrert"
        print "Start the new game"
        new_game()
    elif (num > int(guess)):
        print "Higher"
        remain_guess -= 1
        print "Number of remaining guess is",remain_guess
    elif (num < int(guess)):
        print "Lower"
        remain_guess -= 1
        print "Number of remaining guess is",remain_guess
    
frame = simplegui.create_frame("Guess the number", 200, 200)
frame.add_button("Range is [0, 100]", range100, 200)
frame.add_button("Range is [0, 1000]", range1000, 200)
frame.add_input("Enter a guess", get_input, 200)

new_game()

frame.start()
