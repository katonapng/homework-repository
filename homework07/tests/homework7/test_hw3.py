from homework7.hw3 import tic_tac_toe_checker


def test_row_winner():
    """Test winner in rows"""
    assert tic_tac_toe_checker([['o', 'o', 'o'],
                                ['x', 'x', 'o'],
                                ['-', 'x', 'x']]) == 'o wins!'


def test_column_winner():
    """Test winner in columns"""
    assert tic_tac_toe_checker([['-', 'x', 'o'],
                                ['o', 'x', 'o'],
                                ['o', 'x', 'x']]) == 'x wins!'


def test_left_to_right_diagonal_winner():
    """Test winner in left to right diagonal"""
    assert tic_tac_toe_checker([['x', '-', 'o'],
                                ['o', 'x', 'o'],
                                ['o', 'x', 'x']]) == 'x wins!'


def test_right_to_left_diagonal_winner():
    """Test winner in right to left diagonal"""
    assert tic_tac_toe_checker([['x', 'x', 'o'],
                                ['o', 'o', 'x'],
                                ['o', '-', 'x']]) == 'o wins!'


def test_draw():
    """Test draw"""
    assert tic_tac_toe_checker([['x', 'x', 'o'],
                                ['o', 'o', 'x'],
                                ['x', 'o', 'x']]) == 'draw'


def test_unfinished_board():
    """Test if game is unfinished"""
    assert tic_tac_toe_checker([['x', '-', 'o'],
                                ['-', 'x', '-'],
                                ['x', 'x', 'o']]) == 'unfinished'
