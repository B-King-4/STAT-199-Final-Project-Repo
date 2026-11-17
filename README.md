# STAT 199 Roulette Day in the Life Project

## Description
This projects follows a hypothetical day in my life as a professional roulette gambler. This project functions nearly identically to how you would bet at a roulette table at a normal casino, aside from a few changes to comply with coding bounds. The variable we are tracking for the user's state here is their money they are betting with. If the player wins the bet, they will gain money and come closer to winning the game, which is ultimately when the user makes $1000 after starting from $100. However, if the player loses money, they get closer to losing the game, which happens when they run out of money to bet with and are forced to go home.

## Our Goal
My family has not been on vacation in the last five years, and my son, Timmy, has wanted to go on a family cruise to the Bahamas for his birthday gift. Your normal job as a content creator is no longer cutting the mustard, so you have resorted to professionally playing at the roulette table. Our goal: turn $100 into $1000 and buy our family tickets for a four day cruise to the Bahamas.

## How to Play the Game:

- The player starts out with $100
- Your objective is to 10x your money and make $1000 to go on a family trip
- You will be asked whether you want to bet on a color
- If you do, claim how much money you want to bet
- If not, the next bet prompt will appear
- If you still have money remaining, you will be asked if you want to bet on whether the number will be odd or even
- If you do, claim how much money you want to bet
- As long as you have money, you will be asked all the possible betting prompts on a roulette table, including: 

    - 1-18 or 19-36
    - Dozens
    - Rows
    - Six-Packs
    - Four-Squares
    - Vertical 3 Columns
    - Pairs
    - Single Numbers
- ### Note on Betting Values (If you Win)
    - 2x Money bets: Color, Odd/Even, 1-18/19-36
    - 3x Money bets: Dozens, Rows
    - 6x Money bets: Six-Packs
    - 9x Money bets - Four-Squares
    - 12x Money bets - Vertical 3 Columns
    - 18x Money bets - Pairs
    - 36x Money bets - Single Number 

- After all bets are final, the random number is generated (ball lands on the number IRL)
- If the bet(s) is/are correct, player will be rewarded accordingly to the dictionary of probabilities 
- If the bet(s) is/are incorrect, the money will be taken from the player's money stash
- The user's status is dependent on how much money they have available to bet with
- If the user makes $1000, they win
- If the user loses all their money, they lose

## How is Player State Tracked?
Our player's state is tracked via a check_game_status function found in the dealer_shouts.py file. It checks to see if the player betting is still between $0-$1000 in money amount, which will allow the game to keep playing. It also checks if the player has made more $1000 or more, in which case the player will win, and if the player has $0, in which case they go bankrupt and must return home (they lose). This function is called in our main() function in our roulette.py file, so a function that calls another function is used to determine whether the user has won based on their state (money amount left)
## Files & Functions
We will now give a quick debrief of the Files and Functions found in the repository

## roulette.py
This file contains all of the import functions from the other file as well as the main() function that performs the main gameplay and is the file that needs to be run in order to play the game

- ### main()
    - The main function takes no inputs or outputs, but acts as the driver code for the roulette.py file that constructs the actively gameplay flow. It incorporates many functions from other files mentioned below

## roulette_spin.py
This file contains the function that acts as the roulette spin process in the actual casino

- ### computer_pick_number():
    -This function simulates the roulette spin an picks one of the random 37 numberes on the wheel.

## roulette_identifier_functions.py
This file contains all of the functions that identify which betting groups the number the computer picked belongs to

- ### identify_color():
    - Function that identifies the color associated with the number that the computer chose


- ### identify_odd_or_even():
    - Function that identifies whether the number the computer chose is odd, even, or neither


- ### identify_which_half_number():
    - Function that identifies whether the number the computer chose is in the number set 1-18, 19-36, or neither

- ### identify_dozen():
    - Function that identifies whether the number the computer chose in in the 1st, 2nd, or 3rd Dozen of Number


- ### identify_row():
    - Function that identifies whether the number the computer chose is in the Top, Middle, or Bottom Row of Numbers

- ### identify_six_pack():
    - Function that identifies whether the number the computer chose is a part of any of the potential six-packs layed out on the roulette board


- ### identify_four_square():
    - Function that identifies whether the nubmer the computer chose is a part of any of the potential four-squares layed out on the roulette board


- ### identify_three_column():
    - Function that identifies whether the number the computer chose is a part of any of the vertical columns of 3 numbers layed out on the roulette board


- ### identify_pair():
    - Function that identifies whether the number the computer chose is a part of any of the potential pairs of 2 numbers layed out on the roulette board


- ### identify_single():
    - Function that verifies whether the number the computer chose is the same as the number that the player bet on

## roulette_bets_functions.py
This file contains two functions, one that controls the bet amount by the player, and the other that organizes the type of bets the player wants to make into a dictionary

- ### bet_amount():
    - Function that asks the player how much money they would like to bet for a respective chosen bet


### player_bets():
 - This is the most complex function in my project code. It is responsible for asking the player for what types of bets they would like to place and then organizing them in a dictionary total_bets

## dealer_shouts.py
This file contains three distinct functions. The first simulates random phrases that the dealer might say after the roulette result finishes. The second is inspirational advice to the player based on their game status. The third actually checks the game/player status, and if the player is betwen $0-$1000, then the inspirational advice will kick in.

- ### dealer.announcements()
    - Function that randomly generates dealer phrases after the roulette ball has finished spinning

- ### progress_messages()
    - Function that randomly generates inspirational messages to the player based on the progress the player has made betting so far

- ### check_game_status()
    - Function that determines whether the player has won, lost, or needs to continue playing to determine whether they win or lose. This function is also responsible for generating messgers from progress_messages.

## One Last Note For New Players
Even if playing through a day in my hypothetical life you have never played roulette before, that is okay! Please refer to the earlier steps of how to play the game and look at the dictionary of bet values. Remember, if you win a bet, the dealer still takes your money for the bet, but returns the multiplied values of the bet back to your according to the reference list above. If you lose, the dealer will take all of your bet money. I hope you enjoy a day in my hypothetical life and please let Timmy's get his birthday wish and go on that family cruise!