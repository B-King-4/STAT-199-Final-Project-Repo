"""
Today I am an amatuer gambler, and this is a day in my life.
Today we are going to play roulette with my usual bankroll of $100
Our goal is to 10x our money, so in order to do this we must bet our money carefully
We are playing on a 0/00 wheel.
It is up to the user's input and decision making on 
the amount of money they want to bet that determines
how long they stay in the game to complete their goal.
A spins counter will count how many spins you last with your
current bankroll until you either make $1000 and send your family
on a cruise or lose all of your money and leave the casino.
"""

from roulette_identifier_functions import (
    identify_color,
    identify_odd_or_even,
    identify_which_half_number,
    identify_dozen,
    identify_row,
    identify_six_pack,
    identify_four_square,
    identify_three_column,
    identify_pair,
    identify_single
)

from roulette_bets_functions import (
    player_bets
)

from roulette_spin import(
    computer_pick_number
)

from dealer_shouts import (
    dealer_announcements,
    check_game_status
)

PAYOUTS= {
            "color": 1,
            "odds_evens": 1,
            "halves": 1,
            "dozens": 2,
            "rows": 2,
            "sixpacks": 5,
            "four_square": 8,
            "columns": 11,
            "pairs": 17,
            "single": 35
}

def main():
    """
    Function that runs the main game loop for the who roulette simulation,
    specifically the function that calls the function that tracks
    the player status (bankroll and spin count) until they reach $1000
    or go bankrupt

    Inputs: None
    
    Outputs: None

    Side Effects: Calls many functions within the function to work the game
    
    """

    money = 100
    spin_count = 1
    playing_game_loop = True

    print("""WELCOME to a day in my life as professional roulette 
    gambler!""")
    print("""Our mission is to send our family on a nice cruise,
      which costs $1000""")
    print("""You will start with $100.
    If you manage to turn it into $1000 without going 
    bankrupt, you win the family cruise! However, if 
    you go bankrupt, you lose and must go home""")

    while playing_game_loop:
        print(f"\n We are now at Spin {spin_count} at the casino")
        print(f"Current Money Balance is: ${money:.2f}")

        total_bets, money = player_bets(money)

        print("\n All bets are final, we will now spin the wheel")
        winning_numb = computer_pick_number()
        dealer_announcements(winning_numb)

        spin_results = {
            "color": identify_color(winning_numb),
            "odds_evens": identify_odd_or_even(winning_numb),
            "halves": identify_which_half_number(winning_numb),
            "dozens": identify_dozen(winning_numb),
            "rows": identify_row(winning_numb),
            "sixpacks": identify_six_pack(winning_numb),
            "four_square": identify_four_square(winning_numb),
            "columns": identify_three_column(winning_numb),
            "pairs": identify_pair(winning_numb),
        }

        print("\n Results for Spin:")

        if "color" in total_bets:
            player_choice = total_bets["color"][0]
            wager_amount = total_bets["color"][1]
            if player_choice == spin_results["color"]:
                winnings = wager_amount + wager_amount * PAYOUTS["color"]
                money += winnings
                print(f"Won ${winnings:.2f} on Color {player_choice}")
            else:
                print(f"Lost ${wager_amount:.2f} on Color {player_choice}")


        if "odds_evens" in total_bets:
            player_choice = total_bets["odds_evens"][0]
            wager_amount = total_bets["odds_evens"][1]
            if player_choice == spin_results["odds_evens"]:
                winnings = wager_amount + wager_amount * PAYOUTS["odds_evens"]
                money += winnings
                print(f"Won ${winnings:.2f} on Odds/Evens {player_choice}")
            else:
                print(f"Lost ${wager_amount:.2f} on Odds/Evens {player_choice}")


        if "halves" in total_bets:
            player_choice = total_bets["halves"][0]
            wager_amount = total_bets["halves"][1]
            if player_choice == spin_results["halves"]:
                winnings = wager_amount + wager_amount * PAYOUTS["halves"]
                money += winnings
                print(f"Won ${winnings:.2f} on Half {player_choice}")
            else:
                print(f"Lost ${wager_amount:.2f} on Half {player_choice}")


        if "dozens" in total_bets:
            player_choice = total_bets["dozens"][0]
            wager_amount = total_bets["dozens"][1]
            if player_choice == spin_results["dozens"]:
                winnings = wager_amount + wager_amount * PAYOUTS["dozens"]
                money += winnings
                print(f"Won ${winnings:.2f} on Dozen {player_choice}")
            else:
                print(f"Lost ${wager_amount:.2f} on Dozen {player_choice}")


        if "rows" in total_bets:
            player_choice = total_bets["rows"][0]
            wager_amount = total_bets["rows"][1]
            if player_choice == spin_results["rows"]:
                winnings = wager_amount + wager_amount * PAYOUTS["rows"]
                money += winnings
                print(f"Won ${winnings:.2f} on Row {player_choice}")
            else:
                print(f"Lost ${wager_amount:.2f} on Row {player_choice}")


        if "sixpacks" in total_bets:
            player_choice = total_bets["sixpacks"][0]
            wager_amount = total_bets["sixpacks"][1]
            if player_choice in spin_results["sixpacks"]:
                winnings = wager_amount + wager_amount * PAYOUTS["sixpacks"]
                money += winnings
                print(f"Won ${winnings:.2f} on Sixpack {player_choice}")
            else:
                print(f"Lost ${wager_amount:.2f} on Sixpack {player_choice}")


        if "four_square" in total_bets:
            player_choice = total_bets["four_square"][0]
            wager_amount = total_bets["four_square"][1]
            if player_choice in spin_results["four_square"]:
                winnings = wager_amount + wager_amount * PAYOUTS["four_square"]
                money += winnings
                print(f"Won ${winnings:.2f} on Four Square {player_choice}")
            else:
                print(f"Lost ${wager_amount:.2f} on Four Square {player_choice}")



        if "columns" in total_bets:
            player_choice = total_bets["columns"][0]
            wager_amount = total_bets["columns"][1]
            if player_choice == spin_results["columns"]:
                winnings = wager_amount + wager_amount * PAYOUTS["columns"]
                money += winnings
                print(f"Won ${winnings:.2f} on Column {player_choice}")
            else:
                print(f"Lost ${wager_amount:.2f} on Column {player_choice}")


        if "pairs" in total_bets:
            player_choice = total_bets["pairs"][0]
            wager_amount = total_bets["pairs"][1]
            if player_choice in spin_results["pairs"]:
                winnings = wager_amount + wager_amount * PAYOUTS["pairs"]
                money += winnings
                print(f"Won ${winnings:.2f} on Pair {player_choice}")
            else:
                print(f"Lost ${wager_amount:.2f} on Pair {player_choice}")


        if "single" in total_bets:
            player_choice = total_bets["single"][0]
            wager_amount = total_bets["single"][1]
            is_single = identify_single(player_choice, winning_numb)
            if is_single == "It's a Single Match":
                winnings = wager_amount + wager_amount * PAYOUTS["single"]
                money += winnings
                print(f"Won ${winnings:.2f} on Single {player_choice}")
            else:
                print(f"Lost ${wager_amount:.2f} on Single {player_choice}")



        spin_count += 1
        player_game_loop = check_game_status(money)

        if money >= 1000:
            playing_game_loop = False 
        elif money <= 0:
            playing_game_loop = False 

    if money >= 1000:
        print(f"Congratulations! you have won the game by hitting ${money:.2f} on Spin {spin_count - 1}. See you on the Cruise!")
    else:
        print(f"Oh no! You are out of funds with total funds left of {money:.2f}. You have lost after {spin_count - 1} spins and must return home.")


if __name__ == "__main__":
    main()