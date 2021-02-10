import unittest
import time

# Robot in top left corner cell of grid. Need to get to bottom right.
# Grid is r (row) x c (column). Robot can move either right or down.
# Some cells are "off limits"

class Cell:
    def __init__(self):
        self.off_limit = False

class Grid:
    def __init__(self, row, column):
        self.matrix = [[[Cell()] * column] * row]

    def set_off_limit(self, row, column):
        self.matrix[column][row].off_limit = True

# I am not sure this needs to be a dynamic programming problem.