# template for "Guess the number" mini-project
# input will come from buttons and an input field
# all output for the game will be printed in the console
import random
import simplegui

secret_number = 0
num_range = 100
number_of_guesses = 7
aux_numb_of_guesses = 0

# helper function to start and restart the game
def new_game():
    # initialize global variables used in your code here
    global secret_number
    global aux_numb_of_guesses

    aux_numb_of_guesses = number_of_guesses

    secret_number = random.randrange(num_range)
    print "\nNew game. Range is from 0 to ", num_range
    print "Number of remaining guesses is ", number_of_guesses, "\n"



# define event handlers for control panel
def range100():
    # button that changes the range to [0,100) and starts a new game 
    global number_of_guesses
    global num_range

    num_range = 100

    number_of_guesses = 7

    new_game()

def range1000():
    # button that changes the range to [0,1000) and starts a new game     
    global num_range
    global number_of_guesses

    num_range = 1000

    number_of_guesses = 10

    new_game()
    
def input_guess(guess):
    # main game logic goes here	
    global aux_numb_of_guesses

    guess_number = int(guess)
    aux_numb_of_guesses-= 1

    print("Guess was " + guess)
    print "Number of remaining guesses is ", aux_numb_of_guesses

    if guess_number != secret_number and aux_numb_of_guesses == 0:
        print "You ran out of guesses. The number was ", secret_number
        new_game()
    elif guess_number < secret_number:
        print "Higher\n"
    elif guess_number > secret_number:
        print "Lower\n"
    else:
        print "Correct\n"
        new_game()
    
    
    
# create frame - create the window
frame = simplegui.create_frame("Guess the number", 200, 200)

# register event handlers for control elements and start frame
frame.add_button("Range is [0, 100)", range100, 200)
frame.add_button("Range is [0, 1000)", range1000, 200)
frame.add_input("Enter a guess", input_guess, 200)

# call new_game 
new_game()
frame.start()


# always remember to check your completed program against the grading rubric
