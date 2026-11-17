"""
The following file contains two functions:
One of the functions allows players to choose the amout
of money they want to bet
The second asks players what bets they would like to make
and organizes them into a dictionary
"""

def bet_amount(money):

    """
    Function that asks the player how much money they would like to bet
    for a respective chosen bet

    Input: money - a float of the amount of money the player has

    Output: return amount - a float of the amount of money the player bets

    Side Effects: None
    
    """

    #activates player betting loop
    player_betting = True

    while player_betting:
        try:
            amount = float(input(f"How Much Money Would You Like To Bet? **REMINDER**: Amount Remaining: ${money:.2f}):"))
            if 0 < amount <= money and round(amount,2) == amount:
                return amount
            else:
                print(f"Invalid money amount, must be a float between $0.01 and ${money:.2f} in appropriate dollars and cents")
        except ValueError:
            print(f"Invalid Input! Please enter a numeric money amount between $0.01 and ${money:.2f}")

def player_bets(money):

    """
    This is the most complex function in my project code. It is responsible for
    asking the player for what types of bets they would like to place and
    then organizing them in a dictionary total_bets

    Inputs: money - a float of the amount of money the player has available

    Outputs: total bets, money - a dictionary of the total bets the player made
                                and money, the total amount of money the player
                                has left
    
    Side Effects: Only side effect is that on some of the longer bet options the
                  format python provides in the terminal can give unecessary spaces,
                  however this is necessary to keep the code easy to read in the script itself
    """

    #creates a dictionary to store the total_Bets
    total_bets = {}

    #activates color prompting loop
    color_prompting_active = True
    color_bet = ""
    while color_prompting_active:
        color_bet = input("Would you like to pick a color (y/n)? :")
        if color_bet in ["y", "n"]:
            break
        else:
            print("Error: Type either 'y' or 'n'")
    # if y/n is inputted, it kicks the player out of the prompting loop searching for valid input
    if color_bet == "y":
        choosing_color_active = True
        color_choice = ""
        while choosing_color_active:
            color_choice = input("Choose 'red', or 'black', ").strip().lower()
            if color_choice in ["red", "black"]:
                break
            else:
                print("Invalid argument, please choose 'red', or 'black'")
        amount = bet_amount(money)
        money -= amount
        total_bets["color"] = (color_choice, amount)

    if money > 0:
        odds_prompting_active = True
        odds_bet = ""
        while odds_prompting_active:
            odds_bet = input("Would you like to be on Odds/Evens? (y/n)? :")
            if odds_bet in ["y", "n"]:
                break
            else:
                print("Error: type either 'y' or 'n'")
        if odds_bet == "y":
            choosing_odds_active = True
            odds_choice = ""
            while choosing_odds_active:
                odds_choice = input("Choose 'odd' or 'even': ").strip().lower()
                if odds_choice in ["odd", "even"]:
                    break
                else:
                    print("Invalid argument, choose either 'odd' or 'even' ")
            amount = bet_amount(money)
            money -= amount
            total_bets["odds_evens"] = (odds_choice, amount)

    if money > 0:
        halves_prompting_active = True
        halves_bet = ""
        while halves_prompting_active:
            halves_bet = input("Would you like to bet on numbers 1-18/19-36 (y/n)?: ")
            if halves_bet in ['y', 'n']:
                break
            else:
                print("Error: Type either 'y' or 'n' ")

        if halves_bet == "y":
            choosing_halves_active = True
            halves_choice = ""
            while choosing_halves_active:
                halves_choice = input("Choose '1-18' or '19-36': ").strip()
                if halves_choice in ['1-18', '19-36']:
                    break
                else:
                    print("Invalid argument, choose either '1-18' or '19-36' ")

            amount = bet_amount(money)
            money -= amount
            total_bets["halves"] = (halves_choice, amount)

    if money > 0:
        dozens_prompting_active = True
        dozens_bet = ""
        while dozens_prompting_active:
            dozens_bet = input("Would you like to bet on Dozens (y/n)?: ")
            if dozens_bet in ['y', 'n']:
                break
            else:
                print("Error: Type either 'y' or 'n' ")

        if dozens_bet == "y":
            choosing_dozens_active = True
            dozens_choice = ""
            while choosing_dozens_active:
                dozens_choice = input("Choose '1st Dozen' '2nd Dozen' or '3rd Dozen': ").strip()
                if dozens_choice in ['1st Dozen', '2nd Dozen', '3rd Dozen']:
                    break
                else:
                    print("Invalid argument, choose either '1st Dozen', '2nd Dozen', or '3rd Dozen' ")

            amount = bet_amount(money)
            money -= amount
            total_bets["dozens"] = (dozens_choice, amount)

    if money > 0:
        row_prompting_active = True
        row_bet = ""
        while row_prompting_active:
            row_bet = input("Would you like to bet on a row (y/n)?: ")
            if row_bet in ['y', 'n']:
                break
            else:
                print("Error: Type either 'y' or 'n' ")

        if row_bet == "y":
            choosing_row_active = True
            row_choice = ""
            while choosing_row_active:
                row_choice = input("Choose 'Top Row' 'Middle Row' or 'Bottom Row': ").strip()
                if row_choice in ['Top Row', 'Middle Row', 'Bottom Row']:
                    break
                else:
                    print("Invalid argument, choose either 'Top Row', 'Middle Row', or 'Bottom Row' ")

            amount = bet_amount(money)
            money -= amount
            total_bets["rows"] = (row_choice, amount)

    if money > 0:
        sixpack_prompting_active = True
        sixpack_bet = ""
        while sixpack_prompting_active:
            sixpack_bet = input("Would you like to bet on a sixpack (y/n)?: ")
            if sixpack_bet in ['y', 'n']:
                break
            else:
                print("Error: Type either 'y' or 'n' ")

        if sixpack_bet == "y":
            choosing_sixpack_active = True
            sixpack_choice = ""
            while choosing_sixpack_active:
                sixpack_choice = input("Choose 'Pack 1-6', 'Pack 4-9', 'Pack 7-12', 'Pack 10-15', 'Pack 13-18', \
                'Pack 16-21', 'Pack 19-24', 'Pack 22-27', 'Pack 25-30', 'Pack 28-33', or 'Pack 31-36': ").strip()
                
                if sixpack_choice in ['Pack 1-6', 'Pack 4-9', 'Pack 7-12', 'Pack 10-15', 'Pack 13-18', \
                'Pack 16-21', 'Pack 19-24', 'Pack 22-27', 'Pack 25-30', 'Pack 28-33', 'Pack 31-36']:
                    break
                else:
                    print("Invalid argument, choose either 'Pack 1-6', 'Pack 4-9', 'Pack 7-12', 'Pack 10-15', 'Pack 13-18', \
                    'Pack 16-21', 'Pack 19-24', 'Pack 22-27', 'Pack 25-30', 'Pack 28-33', or 'Pack 31-36' ")

            amount = bet_amount(money)
            money -= amount
            total_bets["sixpacks"] = (sixpack_choice, amount)

    if money > 0:
        foursq_prompting_active = True
        foursq_bet = ""
        while foursq_prompting_active:
            foursq_bet = input("Would you like to bet on a foursquare (y/n)?: ")
            if foursq_bet in ['y', 'n']:
                break
            else:
                print("Error: Type either 'y' or 'n' ")

        if foursq_bet == "y":
            choosing_foursq_active = True
            foursq_choice = ""
            while choosing_foursq_active:
                foursq_choice = input("Choose 'Square 1-2-4-5', 'Square 2-3-5-6', 'Square 4-5-7-8', 'Square 5-6-8-9', \
                'Square 7-8-10-11', 'Square 8-9-11-12', 'Square 10-11-13-14', 'Square 11-12-14-15', \
                'Square 13-14-16-17', 'Square 14-15-17-18', 'Square 16-17-19-20', 'Square 17-18-20-21', \
                'Square 19-20-22-23', 'Square 20-21-23-24', 'Square 22-23-25-26', 'Square 23-24-26-27', \
                'Square 25-26-28-29', 'Square 26-27-29-30', 'Square 28-29-31-32', 'Square 29-30-32-33', \
                'Square 31-32-34-35', or 'Square 32-33-35-36' : ").strip()
                
                if foursq_choice in ['Square 1-2-4-5', 'Square 2-3-5-6', 'Square 4-5-7-8', 'Square 5-6-8-9', \
                'Square 7-8-10-11', 'Square 8-9-11-12', 'Square 10-11-13-14', 'Square 11-12-14-15', \
                'Square 13-14-16-17', 'Square 14-15-17-18', 'Square 16-17-19-20', 'Square 17-18-20-21', \
                'Square 19-20-22-23', 'Square 20-21-23-24', 'Square 22-23-25-26', 'Square 23-24-26-27', \
                'Square 25-26-28-29', 'Square 26-27-29-30', 'Square 28-29-31-32', 'Square 29-30-32-33', \
                'Square 31-32-34-35', 'Square 32-33-35-36']:
                    break
                else:
                    print("Invalid argument, choose either  'Square 1-2-4-5', 'Square 2-3-5-6', 'Square 4-5-7-8', 'Square 5-6-8-9', \
                    'Square 7-8-10-11', 'Square 8-9-11-12', 'Square 10-11-13-14', 'Square 11-12-14-15', \
                    'Square 13-14-16-17', 'Square 14-15-17-18', 'Square 16-17-19-20', 'Square 17-18-20-21', \
                    'Square 19-20-22-23', 'Square 20-21-23-24', 'Square 22-23-25-26', 'Square 23-24-26-27', \
                    'Square 25-26-28-29', 'Square 26-27-29-30', 'Square 28-29-31-32', 'Square 29-30-32-33', \
                    'Square 31-32-34-35', or 'Square 32-33-35-36' ")

            amount = bet_amount(money)
            money -= amount
            total_bets["four_square"] = (foursq_choice, amount)

    if money > 0:
        column_prompting_active = True
        column_bet = ""
        while column_prompting_active:
            column_bet = input("Would you like to bet on a column (y/n)?: ")
            if column_bet in ['y', 'n']:
                break
            else:
                print("Error: Type either 'y' or 'n' ")

        if column_bet == "y":
            choosing_column_active = True
            column_choice = ""
            while choosing_column_active:
                column_choice = input("Choose 'Column 1-2-3', 'Column 4-5-6', 'Column 7-8-9', 'Column 10-11-12', \
                'Column 13-14-15', 'Column 16-17-18', 'Column 19-20-21', 'Column 22-23-24', \
                'Column 25-26-27', 'Column 28-29-30', 'Column 31-32-33', or 'Column 34-35-36' : ").strip()
                
                if column_choice in ['Column 1-2-3', 'Column 4-5-6', 'Column 7-8-9', 'Column 10-11-12', \
                'Column 13-14-15', 'Column 16-17-18', 'Column 19-20-21', 'Column 22-23-24', \
                'Column 25-26-27', 'Column 28-29-30', 'Column 31-32-33', 'Column 34-35-36']:
                    break
                else:
                    print("Invalid argument, choose either  'Column 1-2-3', 'Column 4-5-6', 'Column 7-8-9', 'Column 10-11-12', \
                    'Column 13-14-15', 'Column 16-17-18', 'Column 19-20-21', 'Column 22-23-24', \
                    'Column 25-26-27', 'Column 28-29-30', 'Column 31-32-33', or 'Column 34-35-36' ")

            amount = bet_amount(money)
            money -= amount
            total_bets["columns"] = (column_choice, amount)


    if money > 0:
        pairs_prompting_active = True
        pairs_bet = ""
        while pairs_prompting_active:
            pairs_bet = input("Would you like to bet on a pair (y/n)?: ")
            if pairs_bet in ['y', 'n']:
                break
            else:
                print("Error: Type either 'y' or 'n' ")

        if pairs_bet == "y":
            choosing_pair_active = True
            pair_choice = ""
            while choosing_pair_active:
                pair_choice = input("Choose 'Pair 1-2', 'Pair 2-3', 'Pair 4-5', 'Pair 5-6', 'Pair 7-8', 'Pair 8-9', \
                'Pair 10-11', 'Pair 11-12', 'Pair 13-14', 'Pair 14-15', 'Pair 16-17', 'Pair 17-18', \
                'Pair 19-20', 'Pair 20-21', 'Pair 22-23', 'Pair 23-24', 'Pair 25-26', 'Pair 26-27', \
                'Pair 28-29', 'Pair 29-30', 'Pair 31-32', 'Pair 32-33', 'Pair 34-35', 'Pair 35,36',  \
                'Pair 1-4', 'Pair 2-5', 'Pair 3-6', 'Pair 4-7', 'Pair 5-8', 'Pair 6-9', 'Pair 7-10', \
                'Pair 8-11', 'Pair 9-12', 'Pair 10-13', 'Pair 11-14', 'Pair 12-15', 'Pair 13-16', 'Pair 14-17', \
                'Pair 15-18', 'Pair 16-19', 'Pair 17-20', 'Pair 18-21', 'Pair 19-22', 'Pair 20-23', \
                'Pair 21-24', 'Pair 22-25', 'Pair 23-26', 'Pair 24-27', 'Pair 25-28', 'Pair 26-29', 'Pair 27-30', \
                'Pair 28-31', 'Pair 29-32', 'Pair 30-33', 'Pair 31-34', 'Pair 32-35', 'Pair 33-36', or 'Pair 0-00' : ").strip()
                
                if pair_choice in ['Pair 1-2', 'Pair 2-3', 'Pair 4-5', 'Pair 5-6', 'Pair 7-8', 'Pair 8-9', \
                'Pair 10-11', 'Pair 11-12', 'Pair 13-14', 'Pair 14-15', 'Pair 16-17', 'Pair 17-18', \
                'Pair 19-20', 'Pair 20-21', 'Pair 22-23', 'Pair 23-24', 'Pair 25-26', 'Pair 26-27', \
                'Pair 28-29', 'Pair 29-30', 'Pair 31-32', 'Pair 32-33', 'Pair 34-35', 'Pair 35-36',  \
                'Pair 1-4', 'Pair 2-5', 'Pair 3-6', 'Pair 4-7', 'Pair 5-8', 'Pair 6-9', 'Pair 7-10', \
                'Pair 8-11', 'Pair 9-12', 'Pair 10-13', 'Pair 11-14', 'Pair 12-15', 'Pair 13-16', 'Pair 14-17', \
                'Pair 15-18', 'Pair 16-19', 'Pair 17-20', 'Pair 18-21', 'Pair 19-22', 'Pair 20-23', \
                'Pair 21-24', 'Pair 22-25', 'Pair 23-26', 'Pair 24-27', 'Pair 25-28', 'Pair 26-29', 'Pair 27-30', \
                'Pair 28-31', 'Pair 29-32', 'Pair 30-33', 'Pair 31-34', 'Pair 32-35', 'Pair 33-36', 'Pair 0-00']:
                    break
                else:
                    print("Invalid argument, choose either 'Pair 1-2', 'Pair 2-3', 'Pair 4-5', 'Pair 5-6', 'Pair 7-8', 'Pair 8-9', \
                    'Pair 10-11', 'Pair 11-12', 'Pair 13-14', 'Pair 14-15', 'Pair 16-17', 'Pair 17-18', \
                    'Pair 19-20', 'Pair 20-21', 'Pair 22-23', 'Pair 23-24', 'Pair 25-26', 'Pair 26-27', \
                    'Pair 28-29', 'Pair 29-30', 'Pair 31-32', 'Pair 32-33', 'Pair 34-35', 'Pair 35-36',  \
                    'Pair 1-4', 'Pair 2-5', 'Pair 3-6', 'Pair 4-7', 'Pair 5-8', 'Pair 6-9', 'Pair 7-10', \
                    'Pair 8-11', 'Pair 9-12', 'Pair 10-13', 'Pair 11-14', 'Pair 12-15', 'Pair 13-16', 'Pair 14-17', \
                    'Pair 15-18', 'Pair 16-19', 'Pair 17-20', 'Pair 18-21', 'Pair 19-22', 'Pair 20-23', \
                    'Pair 21-24', 'Pair 22-25', 'Pair 23-26', 'Pair 24-27', 'Pair 25-28', 'Pair 26-29', 'Pair 27-30', \
                    'Pair 28-31', 'Pair 29-32', 'Pair 30-33'. 'Pair 31-34', 'Pair 32-35', 'Pair 33-36', or 'Pair 0-00' ")

            amount = bet_amount(money)
            money -= amount
            total_bets["pairs"] = (pair_choice, amount)

    if money > 0:
        single_prompting_active = True
        single_bet = ""
        while single_prompting_active:
            single_bet = input("Would you like to bet on a single number (y/n)?: ")
            if single_bet in ['y', 'n']:
                break
            else:
                print("Error: Type either 'y' or 'n' ")

        if single_bet == "y":
            choosing_single_active = True
            single_choice = ""
            while choosing_single_active:
                try:
                    single_choice = int(input("Choose an integer -1 through 36 where -1 stands as a placeholder for 00"))

                    if -1 <= single_choice <= 36:
                        break
                    else:
                        print("Invalid argument, choose an integer between -1 and 36")
                except ValueError:
                    print("Invalide input! Please enter an interger between -1 and 36")

            amount = bet_amount(money)
            money -= amount
            total_bets["single"] = (single_choice, amount)

    return total_bets, money