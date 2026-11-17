"""
The following file contains three functions. Two of which
Incoporate random dealer sayings and inspirational messages
based on the results from the spin and money left. The third is
a function that checks the player's state and helps determine
whether they won or lost the game
"""

import random

def dealer_announcements(winning_numb):
    """
    Function that prints random casino dealer phrases
    after the wheel lands on the number

    Inputs: winning_numb - an integer between -1 and 36 
                            from the spin
    
    Outputs: randomly selected string of a list of potential
                      dealer phrases

    Side effects: None

    """

    numb = winning_numb
    phrases = [
        f"No more bets! Our winning number is {numb}!",
        f"All bets are final! Our winning number is {numb}",
        f"The dealers says our lucky winner is {numb}!",
        f"Round and Round she goes and its going to be a {numb}! "
    ]
    print(random.choice(phrases))


def progress_messages(money):
    """
    Function that prints a randomized message based on
    how close the player's bankroll is to the $1,000 goal
    of the family cruise

    Inputs: money - float that represents the players current
                    money balance in dollars
    
    Outputs: randomly selected string of a list of potential progress
                messages

    Side Effects: None

    """

    if money >= 500:
        messages = [
            "You are almost there! keep betting!",
            "Family vacation in sight! Keep betting!",
            "Holy smokes! You are on fire!"
        ]

    else:
        messages = [
            "Keep Going! All it takes is a little luck!",
            "Family cruise is in the near future!",
            "Keep betting for the family!"
        ]
    print(random.choice(messages))

def check_game_status(money):
    """
    Function that determines whether the player has won
    or lost ($1000+ or $0) and this will determine whether
    we still generate the progress messages

    Inputs: money - a float that is the current player's balance

    Outputs: boolean True if game should keep running or False if won/lost

    Side Effects: Calls cruise_progress_message() when the game continues

    """

    if money >= 1000:
        return False
    elif money <= 0:
        return False
    else:
        progress_messages(money)
        return True