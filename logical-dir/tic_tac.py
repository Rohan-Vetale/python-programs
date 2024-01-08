'''

@Author: Rohan Vetale

@Date: 2023-01-04 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-04 16:00:30

@Title : Tic Tac Toe game


'''

import random

# Tic Tac Toe game
player_moves = []
pc_moves = []

def print_board():
    """
        Description:
        This function is used to print the board

        Parameter:
        None

        Return:
        It does not return anything but prints the board
    """
    for i in range(1, 4):
        for j in range(1, 4):
            if (i, j) in player_moves:
                print("X", end=" ")
            elif (i, j) in pc_moves:
                print("O", end=" ")
            else:
                print("-", end=" ")
        print()

def check_winner():
    winning_combinations = [
        [(1, 1), (1, 2), (1, 3)],
        [(2, 1), (2, 2), (2, 3)],
        [(3, 1), (3, 2), (3, 3)],
        [(1, 1), (2, 1), (3, 1)],
        [(1, 2), (2, 2), (3, 2)],
        [(1, 3), (2, 3), (3, 3)],
        [(1, 1), (2, 2), (3, 3)],
        [(1, 3), (2, 2), (3, 1)]
    ]

    for combination in winning_combinations:
        if all(move in player_moves for move in combination):
            return "Player (You) wins!"
        elif all(move in pc_moves for move in combination):
            return "Computer wins!"
    
    return None

while True:
    pl_move_x = int(input("Enter the row to put your X (1, 2, 3) "))
    if pl_move_x == 0:
        # Quit the game
        break
    pl_move_y = int(input("Enter the col to put your X (1, 2, 3) "))

    space_check = (pl_move_x, pl_move_y)

    # Check whether the space is already occupied by player or pc
    if space_check in player_moves or space_check in pc_moves:
        print("The space is already occupied, please try other space ")
    else:
        player_moves.append(space_check)
        print(f"Added X to {space_check}")
        print_board()

        # Check for a winner
        result = check_winner()
        if result:
            print(result)
            break

        print("Now it is computer's turn: ")

        # Computer's move
        while True:
            pc_move_x = random.randint(1, 3)
            pc_move_y = random.randint(1, 3)
            pc_space_check = (pc_move_x, pc_move_y)

            if pc_space_check not in player_moves and pc_space_check not in pc_moves:
                pc_moves.append(pc_space_check)
                print(f"Computer added O to {pc_space_check}")
                print_board()

                # Check for a winner
                result = check_winner()
                if result:
                    print(result)
                    break

                break


