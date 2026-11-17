"""
This file contains the function that simulates the roulette spin
"""

import random

def computer_pick_number():
    """
    Generates a random integer between -1 through 36, or where -1
    represents the 00 on the board, probably using a built 
    in random number generator from python.
    
    Inputs: None (using a random pick number)
    
    Outputs: numb: returns a random integer -1 - 36
        
    """
    computer_number = random.randint(-1,36)
    return computer_number