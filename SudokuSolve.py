# Sudoku Solver -- Solves a unsolved_sudoku puzzle with recursion and back
# tracking.

# Author (Pieced together from the internet by): Raleigh Martin
# Date: 5-11-20

import numpy as np
import re

# For generating puzzles from the pattern

############################################################
generate_puzzle = False

appearance_pattern = [['*', '*', '*', 'x', '*', 'x', '*', '*', '*'],
                      #             ||             ||            ||
                      ['*', '*', '*', 'x', '*', 'x', '*', '*', '*'],
                      #             ||             ||            ||
                      ['*', 'x', '*', '*', '*', '*', '*', 'x', '*'],
                      # ------------##-------------##------------||
                      ['x', 'x', '*', '*', '*', '*', '*', 'x', 'x'],
                      #             ||             ||            ||
                      ['*', '*', '*', '*', 'x', '*', '*', '*', '*'],
                      #             ||             ||            ||
                      ['x', 'x', '*', '*', '*', '*', '*', 'x', 'x'],
                      # ------------##-------------##------------ #
                      ['*', 'x', '*', '*', '*', '*', '*', 'x', '*'],
                      #             ||             ||            ||
                      ['*', '*', '*', 'x', '*', 'x', '*', '*', '*'],
                      #             ||             ||            ||
                      ['*', '*', '*', 'x', '*', 'x', '*', '*', '*']]


############################################################
unsolved_sudoku = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
                   [6, 0, 0, 1, 9, 5, 0, 0, 0],
                   [0, 9, 8, 0, 0, 0, 0, 6, 0],
                   [8, 0, 0, 0, 6, 0, 0, 0, 3],
                   [4, 0, 0, 8, 0, 3, 0, 0, 1],
                   [7, 0, 0, 0, 2, 0, 0, 0, 6],
                   [0, 6, 0, 0, 0, 0, 2, 8, 0],
                   [0, 0, 0, 4, 1, 9, 0, 0, 5],
                   [0, 0, 0, 0, 8, 0, 0, 7, 9]]

very_basic_sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 7],
                     [7, 2, 0, 3, 0, 9, 0, 0, 1],
                     [0, 0, 8, 7, 0, 5, 0, 6, 0],
                     [5, 0, 2, 8, 9, 0, 0, 0, 0],
                     [0, 4, 0, 5, 0, 1, 0, 9, 0],
                     [0, 0, 0, 0, 6, 3, 7, 0, 5],
                     [0, 3, 0, 9, 0, 6, 1, 0, 0],
                     [2, 0, 0, 1, 0, 7, 0, 5, 3],
                     [9, 0, 0, 0, 0, 0, 0, 0, 0]]

empty_sudoku = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0, 0]]

dads_sudoku = [[0, 0, 0, 0, 6, 0, 0, 0, 0],
               [0, 0, 6, 2, 0, 4, 9, 0, 0],
               [0, 7, 0, 0, 0, 0, 0, 4, 0],
               [0, 3, 0, 9, 0, 1, 0, 8, 0],
               [2, 0, 0, 0, 3, 0, 0, 0, 4],
               [0, 9, 0, 6, 0, 2, 0, 5, 0],
               [0, 8, 0, 0, 0, 0, 0, 7, 0],
               [0, 0, 9, 8, 0, 3, 1, 0, 0],
               [0, 0, 0, 0, 2, 0, 0, 0, 0]]

puzzle_to_solve = very_basic_sudoku

steps_to_solve = 0


def is_possible(x, y, guess, sudoku):
    # Define how boxes in sudoku puzzles work
    box_x = (x // 3) * 3
    box_y = (y // 3) * 3

    # Tests if guess is already in col of coords
    for i in range(0, 9):
        if sudoku[i][y] == guess:
            return False

    # Tests if guess is already in row of coords
    for i in range(0, 9):
        if sudoku[x][i] == guess:
            return False

    # Tests if guess is already in the box of coords
    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[box_x + i][box_y + j] == guess:
                return False
    # Everything Passed
    return True


def find_solution(puzzle):
    global steps_to_solve
    possible_solution = False
    for o in range(9):
        for p in range(9):
            if puzzle[o][p] == 0:
                for q in range(1, 10):
                    if is_possible(o, p, q, puzzle):
                        # For Testing each step.
                        # print(str(puzzle[o][p]) + " set to " + str(q))
                        puzzle[o][p] = q
                        steps_to_solve = steps_to_solve + 1
                        possible_solution = True
                        if find_solution(puzzle):
                            return True
                        else:
                            # If we hit a dead end with guesses, we need to set it back
                            # to 0 and start over.
                            puzzle[o][p] = 0
                            # For testing each step.
                            # print(str(puzzle[o][p]) + " reset to 0")
                return False
    return True


find_solution(puzzle_to_solve)

# If we don't want to generate a puzzle then this will display the solution,
# otherwise it will take the solution and remove numbers based on the appearance_pattern
# variable.

if not generate_puzzle:
    solution_string = re.sub("(\\[\\[|\\]|\\s\\[)+", "", str(np.matrix(puzzle_to_solve)))
    print()
    print(solution_string)
    print()
    print("This Sudoku took " + str(steps_to_solve) + " steps to solve.")
else:
    for w in range(9):
        for e in range(9):
            if appearance_pattern[w][e] == '*':
                puzzle_to_solve[w][e] = 0
    new_puzzle = re.sub("(\\[\\[|\\]|\\s\\[)+", "", str(np.matrix(puzzle_to_solve)))
    new_puzzle = re.sub("0", " ", new_puzzle)
    print("\nHere is your Generated Puzzle: \n")
    print(new_puzzle)
