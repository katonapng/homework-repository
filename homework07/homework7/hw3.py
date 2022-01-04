"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [[-, -, o],
     [-, x, o],
     [x, o, x]]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def check_rows(board):
    for row in board:
        unique_elements = set(row)
        if unique_elements != set('-') and len(unique_elements) == 1:
            return unique_elements.pop()
    return False


def check_diagonals(board):
    diagonal_right = [cell[i] for i, cell in enumerate(board)]
    if len(set(diagonal_right)) == 1:
        return diagonal_right.pop()
    diagonal_left = [cell[::-1][i] for i, cell in enumerate(board)]
    if len(set(diagonal_left)) == 1:
        return diagonal_left.pop()
    return False


def check_finish(board):
    for row in board:
        if '-' in row:
            return False
    return True


def tic_tac_toe_checker(board: List[List]) -> str:
    for new_board in (board, list(map(list, zip(*board)))):
        row = check_rows(new_board)
        if row:
            return f'{row} wins!'

    diagonal = check_diagonals(new_board)
    if diagonal:
        return f'{diagonal} wins!'
    if check_finish(board):
        return 'draw'
    return 'unfinished'
