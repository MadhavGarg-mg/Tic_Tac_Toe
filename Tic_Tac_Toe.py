"""I will be making an interactive tik tak tok game"""

def display(row1: list, row2: list, row3: list):
    """
    This function will display the tic tak toe board.
    """
    print(row1)
    print(row2)
    print(row3)


def check_win(lst1: list, lst2: list, lst3: list):
    """
    The function checks if the player has won.
    """
    if lst1[0] == lst2[0] == lst3[0] == 'X' or lst1[0] == lst2[0] == lst3[0] == 'O':
        return True
    elif lst1[1] == lst2[1] == lst3[1] == 'X' or lst1[1] == lst2[1] == lst3[1] == 'O':
        return True
    elif lst1[2] == lst2[2] == lst3[2] == 'X' or lst1[2] == lst2[2] == lst3[2] == 'O':
        return True
    elif lst1[0] == lst2[1] == lst3[2] == 'X' or lst1[0] == lst2[1] == lst3[2] == 'O':
        return True
    elif lst1[2] == lst2[1] == lst3[0] == 'X' or lst1[2] == lst2[1] == lst3[0] == 'O':
        return True


"""Need to add a win condition."""

# def check_winner(row1: list, row2: list, row3: list):
#     """Checks the winner"""
#     for i in range(1, 4):
#         thing = [row1, row2, row3]
#         if (thing[1][i] and thing[2][i] and thing[3][i]) == 'X':
#             print('Player 1 won!')
#             break
#         elif thing[1][i] and thing[2][i] and thing[3][i] == 'O':
#             print('Player 2 won!')
#             break
#         elif thing[i][1] and thing[i][2] and thing[i][3] == 'X':
#             print('Player 1 won!')
#             break
#         elif thing[i][1] and thing[i][2] and thing[i][3] == 'O':
#             print('Player 2 won!')
#             break
#         elif thing[1][1] and thing[2][2] and thing[3][3] == 'X':
#             print('Player 1 won!')
#             break
#         elif thing[1][1] and thing[2][2] and thing[3][3] == 'O':
#             print('Player 2 won!')
#             break
#         elif (thing[1][3] and thing[2][2] and thing[3][1]) == 'X':
#             print('Player 1 won!')
#             break
#         elif (thing[1][3] and thing[2][2] and thing[3][1]) == 'O':
#             print('Player 2 won!')
#             break
#         else:
#             pass


# player_or_comp = input('Will you like to play against a play or the computer?: p or c \n').lower()
# possible = ['p', 'c']
# while player_or_comp not in possible:
#     print(player_or_comp)
#     print('Invalid input!')
#     player_or_comp = input(
#         'Will you like to play against a play or the computer?: p or c \n').lower()


# if player_or_comp == 'p':
display([1, 2, 3], [4, 5, 6], [7, 8, 9])
count = 1
board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
player1_marker = input('Player 1 choose your marker: X or O').upper()

while count < 10:
    if count % 2 != 0:
        print('Player 1')
        p1_row = int(input('What row would you like to choose?: \n'))
        while p1_row > 3:
            print('Invalid row. Try again')
            p1_row = int(input('What row would you like to choose?: \n'))
        p1_column = int(input('What column would you like to choose?: \n'))
        while p1_column > 3:
            print('Invalid column. Try again')
            p1_column = int(input('What column would you like to choose?: \n'))

        while board[p1_row - 1][p1_column - 1] != ' ':
            print('Invalid row and column. Try again')
            p1_row = int(input('What row would you like to choose?: \n'))
            p1_column = int(input('What column would you like to choose?: \n'))

        board[p1_row - 1][p1_column - 1] = player1_marker
        display(board[0], board[1], board[2])
        count += 1
        if check_win(board[0], board[1], board[2]) is True:
            print('Congratulations Player 1! You win!')
            break
        else:
            pass
    else:
        print('Player 2')
        p2_row = int(input('What row would you like to choose?: \n'))
        while p2_row > 3:
            print('Invalid row. Try again')
            p2_row = int(input('What row would you like to choose?: \n'))
        p2_column = int(input('What column would you like to choose?: \n'))
        while p2_column > 3:
            print('Invalid column. Try again')
            p2_column = int(input('What column would you like to choose?: \n'))

        while board[p2_row - 1][p2_column - 1] != ' ':
            print('Invalid row and column. Try again')
            p2_row = int(input('What row would you like to choose?: \n'))
            p2_column = int(input('What column would you like to choose?: \n'))
        if player1_marker == 'X':
            player2_marker = 'O'
        else:
            player2_marker = 'X'
        board[p2_row - 1][p2_column - 1] = player2_marker
        display(board[0], board[1], board[2])
        count += 1
        if check_win(board[0], board[1], board[2]) is True:
            print('Congratulations Player 2! You win!')
            break
        else:
            pass
    # check_winner(board[0], board[1], board[2])

# else:
#     display([1, 2, 3], [4, 5, 6], [7, 8, 9])
#     count = 1
#     thing = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
#     while count < 10 or game_status != 'won':
#         if count % 2 != 0:
#             print('Player 1')
#             p1_row = int(input('What row would you like to choose?: \n'))
#             while p1_row > 3:
#                 print('Invalid row. Try again')
#                 p1_row = int(input('What row would you like to choose?: \n'))
#             p1_column = int(input('What column would you like to choose?: \n'))
#             while p1_column > 3:
#                 print('Invalid column. Try again')
#                 p1_column = int(input('What column would you like to choose?: \n'))
#
#             while thing[p1_row - 1][p1_column - 1] != ' ':
#                 print('Invalid row and column. Try again')
#                 p1_row = int(input('What row would you like to choose?: \n'))
#                 p1_column = int(input('What column would you like to choose?: \n'))
#
#             thing[p1_row - 1][p1_column - 1] = 'X'
#             display(thing[0], thing[1], thing[2])
#             count += 1
#         else:
#             print('Player 2')
#             comp_row = random.randint(1, 3)
#             # p2_row = int(input('What row would you like to choose?: \n'))
#             # while p2_row > 3:
#             #     print('Invalid row. Try again')
#             #     p2_row = int(input('What row would you like to choose?: \n'))
#             comp_column = random.randint(1, 3)
#             # p2_column = int(input('What column would you like to choose?: \n'))
#             # while p2_column > 3:
#             #     print('Invalid column. Try again')
#             #     p2_column = int(input('What column would you like to choose?: \n'))
#
#             while thing[comp_row - 1][comp_column - 1] != ' ':
#                 comp_row = random.randint(1, 3)
#                 comp_column = random.randint(1, 3)
#             #     print('Invalid row and column. Try again')
#             #     p2_row = int(input('What row would you like to choose?: \n'))
#             #     p2_column = int(input('What column would you like to choose?: \n'))
#
#             thing[comp_row - 1][comp_column - 1] = 'O'
#             display(thing[0], thing[1], thing[2])
#             count += 1


# options to play (computer vs player, or player vs player)
