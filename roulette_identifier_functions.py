"""
The following file contains all of the necessary Roulette
Board bet identifying functions (functions that determine
whether the player's input bet "hit" or not) 

"""

def identify_color(numb):

    """
    Function that identifies the color associated with the number
    that the computer chose
    
    It is important to note that 0 and -1 (disguised as 00)
    take the color green
    
    Inputs: numb: an integer between -1 and 36
    
    Outputs:  return color (string of either red, black, or green)

    Side Effects: None
        
    """
    
    if numb in [1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23,
                25, 27, 30, 32, 34, 36]:
        return "red"
    
    elif numb in [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24,
                26, 28, 29, 31, 33, 35]: 
        return "black"
    
    else :
        return "green"

def identify_odd_or_even(numb):

    """
    Function that identifies whether the number the computer chose
    is odd, even, or neither
        
    It is important to note that 0 and -1 (disguised as 00)
    are not denoted as odd or even
        
    Inputs: numb: an integer between -1 and 36
        
    Outputs:  return odd_or_even (string of either odd, even, or neither)

    Side Effects: None
    
    """

    if numb in [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23,
                25, 27, 29, 31, 33, 35]:
        return "odd"

    elif numb in [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22,
                24, 26, 28, 30, 32, 34, 36]:
        return "even"

    else:
        return "N/A odd/even"


def identify_which_half_number(numb):

    """
    Function that identifies whether the number the computer chose
    is on the first 1-18 half of the board or the second 19-36 half
    of the board, or neither
    
    It is important to note that 0 and -1 (disguised as 00)
    are not denoted in either half (house's edge)
    
    Inputs: numb: an integer between -1 and 36
    
    Outputs:  return half_num (string of either 1-18, 19-36, or neither)

    Side Effects: None

    """

    if numb in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13,
                14, 15, 16, 17, 18]:
        return "1-18"
    elif numb in [19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
                30, 31, 32, 33, 34, 35, 36]:
        return "19-36"
    else:
        return "N/A Half"

def identify_dozen(numb):

    """
    Function that identifies whether the computer chosen number is in the 1st, 2nd,
    or 3rd dozen

    Inputs: numb an integer between -1 and 36

    Outputs: return dozen (string of either 1st Dozen, 2nd Dozen, 3rd Dozen, or N/A)

    Side Effects: None

    """

    if numb in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]:
        return "1st Dozen"
    elif numb in [13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]:
        return "2nd Dozen"
    elif numb in [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36]:
        return "3rd Dozen"
    else:
        return "N/A Dozen"

def identify_row(numb):
    """
    Function that identifies whether the computer chosen number is in the Top, Middle,
    or Bottom horizontal row

    Inputs: numb an integer between -1 and 36

    Outputs: return row (string of either Top Row, Middle Row, Bottom Row, or N/A Row)

    Side Effects: None

    """

    if numb in [3, 6, 9, 12, 15, 18, 21, 24, 27, 30, 33, 36]:
        return "Top Row"
    elif numb in [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]:
        return "Middle Row"
    elif numb in [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34]:
        return "Bottom Row"
    else:
        return "N/A Row"

def identify_six_pack(numb):
    """
    Function that identifies whether the computer chosen number is in either of the
    potential 6 packs on the board

    Inputs: numb as an integer between -1 and 36

    Outputs: return six_pack (string of any of the potential six-pack in the
                              form Pack a-b)
    
    Side Effects: None
    """


    winning_packs = []
    if 1 <= numb <= 6:
        winning_packs.append("Pack 1-6")
    if 4 <= numb <=9:
        winning_packs.append("Pack 4-9")
    if 7 <= numb <=12:
        winning_packs.append("Pack 7-12")
    if 10 <= numb <= 15:
        winning_packs.append("Pack 10-15")
    if 13 <= numb <= 18:
        winning_packs.append("Pack 13-18")
    if 16 <= numb <= 21:
        winning_packs.append("Pack 16-21")
    if 19 <= numb <= 24:
        winning_packs.append("Pack 19-24")
    if 22 <= numb <= 27:
        winning_packs.append("Pack 22-27")
    if 25 <= numb <= 30:
        winning_packs.append("Pack 25-30")
    if 28 <= numb <= 33:
        winning_packs.append("Pack 28-33")
    if 31 <= numb <= 36:
        winning_packs.append("Pack 31-36")
    if -1 <= numb <= 0:
        return "No Six Pack Applicable"
    return winning_packs

def identify_four_square(numb):

    """
    Function that identifies whether the computer chosen number is in the many potential
    four-square clusters

    Inputs: numb as an integer between -1 and 36

    Outputs: return four_square (string of either of the potential four_squares
                                 in the form Square a-b-c-d)
    
    Side Effects: None

    """


    winning_squares = []
    if numb in [1, 2, 4, 5]:
        winning_squares.append("Square 1-2-4-5")
    if numb in [2, 3, 5, 6]:
        winning_squares.append("Square 2-3-5-6")
    if numb in [4, 5, 7, 8]:
        winning_squares.append("Square 4-5-7-8")
    if numb in [5, 6, 8, 9]:
        winning_squares.append("Square 5-6-8-9")
    if numb in [7, 8, 10, 11]:
        winning_squares.append("Square 7-8-10-11")
    if numb in [8, 9, 11, 12]:
        winning_squares.append("Square 8-9-11-12")
    if numb in [10, 11, 13, 14]:
        winning_squares.append("Square 10-11-13-14")
    if numb in [11, 12, 14, 15]:
        winning_squares.append("Square 11-12-14-15")
    if numb in [13, 14, 16, 17]:
        winning_squares.append("Square 13-14-16-17")
    if numb in [14, 15, 17, 18]:
        winning_squares.append("Square 14-15-17-18")
    if numb in [16, 17, 19, 20]:
        winning_squares.append("Square 16-17-19-20")
    if numb in [17, 18, 20, 21]:
        winning_squares.append("Square 17-18-20-21")
    if numb in [19, 20, 22, 23]:
        winning_squares.append("Square 19-20-22-23")
    if numb in [20, 21, 23, 24]:
        winning_squares.append("Square 20-21-23-24")
    if numb in [22, 23, 25, 26]:
        winning_squares.append("Square 22-23-25-26")
    if numb in [23, 24, 26, 27]:
        winning_squares.append("Square 23-24-26-27")
    if numb in [25, 26, 28, 29]:
        winning_squares.append("Square 25-26-28-29")
    if numb in [26, 27, 29, 30]:
        winning_squares.append("Square 26-27-29-30")
    if numb in [28, 29, 31, 32]:
        winning_squares.append("Square 28-29-31-32")
    if numb in [29, 30, 32, 33]:
        winning_squares.append("Square 29-30-32-33")
    if numb in [31, 32, 34, 35]:
        winning_squares.append("Square 31-32-34-35")
    if numb in [32, 33, 35, 36]:
        winning_squares.append("Square 32-33-35-36")
    if numb in [-1, 0]:
        return "No Square Available"
    return winning_squares

def identify_three_column(numb):

    """
    Function that Identifies whether the computer chosen number is in the 12 potential
    3 number columns

    Inputs: numb, an integer between -1 and 36

    Outputs: return column, (string of either of the potential vertical columns
                             of the form Column a-b-c)
    
    Side Effects: None
    """


    if numb in [1, 2, 3]:
        return "Column 1-2-3"
    if numb in [4, 5, 6]:
        return "Column 4-5-6"
    if numb in [7, 8, 9]:
        return "Column 7-8-9"
    if numb in [10, 11, 12]:
        return "Column 10-11-12"
    if numb in [13, 14, 15]:
        return "Column 13-14-15"
    if numb in [16, 17, 18]:
        return "Column 16-17-18"
    if numb in [19, 20, 21]:
        return "Column 19-20-21"
    if numb in [22, 23, 24]:
        return "Column 22-23-24"
    if numb in [25, 26, 27]:
        return "Column 25-26-27"
    if numb in [28, 29, 30]:
        return "Column 28-29-30"
    if numb in [31, 32, 33]:
        return "Column 31-32-33"
    if numb in [34, 35, 36]:
        return "Column 34-35-36"
    if numb in [-1,0]:
        return "No Column Available"

def identify_pair(numb):

    """
    Function that identifies whether the computer chosen number is one of the
    possible double pairs.

    Inputs: numb, an integer between -1 and 36

    Outputs: return pair (a string of any of the possible matching pairs
                          associated with the number in the form Pair a-b)

    Side Effects: None
    """


    winning_pairs = []
    if numb in [1,2]:
       winning_pairs.append("Pair 1-2")
    if numb in [2,3]:
        winning_pairs.append("Pair 2-3")
    if numb in [4,5]:
        winning_pairs.append("Pair 4-5")
    if numb in [5,6]:
        winning_pairs.append("Pair 5-6")
    if numb in [7,8]:
       winning_pairs.append("Pair 7-8")
    if numb in [8,9]:
        winning_pairs.append("Pair 8-9")
    if numb in [10,11]:
        winning_pairs.append("Pair 10-11")
    if numb in [11,12]:
        winning_pairs.append("Pair 11-12")
    if numb in [13,14]:
       winning_pairs.append("Pair 13-14")
    if numb in [14,15]:
        winning_pairs.append("Pair 14-15")
    if numb in [16,17]:
        winning_pairs.append("Pair 16-17")
    if numb in [17,18]:
        winning_pairs.append("Pair 17-18")
    if numb in [19,20]:
       winning_pairs.append("Pair 19-20")
    if numb in [20,21]:
        winning_pairs.append("Pair 20-21")
    if numb in [22,23]:
        winning_pairs.append("Pair 22-23")
    if numb in [23,24]:
        winning_pairs.append("Pair 23-24")
    if numb in [25,26]:
       winning_pairs.append("Pair 25-26")
    if numb in [26,27]:
        winning_pairs.append("Pair 26-27")
    if numb in [28,29]:
        winning_pairs.append("Pair 28-29")
    if numb in [29,30]:
        winning_pairs.append("Pair 29-30")
    if numb in [31,32]:
       winning_pairs.append("Pair 31-32")
    if numb in [32,33]:
        winning_pairs.append("Pair 32-33")
    if numb in [34,35]:
        winning_pairs.append("Pair 34-35")
    if numb in [35,36]:
        winning_pairs.append("Pair 35-36")
    if numb in [1,4]:
       winning_pairs.append("Pair 1-4")
    if numb in [2,5]:
        winning_pairs.append("Pair 2-5")
    if numb in [3,6]:
        winning_pairs.append("Pair 3-6")
    if numb in [4,7]:
        winning_pairs.append("Pair 4-7")
    if numb in [5,8]:
       winning_pairs.append("Pair 5-8")
    if numb in [6,9]:
        winning_pairs.append("Pair 6-9")
    if numb in [7,10]:
        winning_pairs.append("Pair 7-10")
    if numb in [8,11]:
        winning_pairs.append("Pair 8-11")
    if numb in [9,12]:
       winning_pairs.append("Pair 9-12")
    if numb in [10,13]:
        winning_pairs.append("Pair 10-13")
    if numb in [11,14]:
        winning_pairs.append("Pair 11-14")
    if numb in [12,15]:
        winning_pairs.append("Pair 12-15")
    if numb in [13,16]:
       winning_pairs.append("Pair 13-16")
    if numb in [14,17]:
        winning_pairs.append("Pair 14-17")
    if numb in [15,18]:
        winning_pairs.append("Pair 15-18")
    if numb in [16,19]:
        winning_pairs.append("Pair 16-19")
    if numb in [17,20]:
       winning_pairs.append("Pair 17-20")
    if numb in [18,21]:
        winning_pairs.append("Pair 18-21")
    if numb in [19,22]:
        winning_pairs.append("Pair 19-22")
    if numb in [20,23]:
        winning_pairs.append("Pair 20-23")
    if numb in [21,24]:
       winning_pairs.append("Pair 21-24")
    if numb in [22,25]:
        winning_pairs.append("Pair 22-25")
    if numb in [23,26]:
        winning_pairs.append("Pair 23-26")
    if numb in [24,27]:
        winning_pairs.append("Pair 24-27")
    if numb in [25,28]:
       winning_pairs.append("Pair 25-28")
    if numb in [26,29]:
        winning_pairs.append("Pair 26-29")
    if numb in [27,30]:
        winning_pairs.append("Pair 27-30")
    if numb in [28,31]:
        winning_pairs.append("Pair 28-31")
    if numb in [29,32]:
       winning_pairs.append("Pair 29-32")
    if numb in [30,33]:
        winning_pairs.append("Pair 30-33")
    if numb in [31,34]:
        winning_pairs.append("Pair 31-34")
    if numb in [32,35]:
        winning_pairs.append("Pair 32-35")
    if numb in [33,36]:
       winning_pairs.append("Pair 33-36")
    if numb in [-1,0]:
        winning_pairs.append("Pair 0-00")
    return winning_pairs

def identify_single(player_numb, computer_numb):

    """
    Function that Identifies whether the computer chosen number
    matches the player chosen number

    Inputs: player_numb and computer_numb: both integers between
    -1 and 36

    Outputs: return match (string of either "It's a Single Match" or
                          "Not a single match")
    
    Side Effects: None
    """

    if player_numb == computer_numb:
        return "It's a Single Match"
    else:
        return "Not a Single Match"