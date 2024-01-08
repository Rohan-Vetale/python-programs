'''

@Author: Rohan Vetale

@Date: 2023-01-04 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-04 16:00:30

@Title : Simulate gambling and print the wins and winning percentage

'''

import random

def gamble(stake, goal):
    """
        Description:
        This function is used to do gamble

        Parameter:
        stake : The total money one has in dollars
        goal : The money aim of the player

        Return:
        wins : Number of times the player won
        bets : Number of bets player played
        win_perecentage : Percentage of wins that player had
    """
    cash = stake
    bets = 0
    wins = 0

    while cash > 0 and cash < goal:
        bets += 1
        if random.choice([True, False]):  # Simulate a fair $1 bet (50% chance of winning)
            cash += 1
            wins += 1
        else:
            cash -= 1

    win_percentage = (wins / bets) * 100 if bets > 0 else 0
    return wins, bets, win_percentage


    
stake = int(input("Enter the cash you have for betting: "))
goal = int(input("What is your money goal in gambling?: "))
experiments = int(input("How many number of experiments do you want?: "))

for i in range(1,experiments+1):
    wins, bets, win_percentage = gamble(stake=stake,goal=goal)
    print(f"Wins are : {wins} ,  Bets were: {bets}, and winning percentage is {win_percentage} for experiment number {i}")

