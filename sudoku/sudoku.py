#!/usr/bin/env python3

"""
Simple Useless script to calculate the golden number
"""

import argparse
import os
import sys

__author__ = 'obayemi'


class Sudoku:
    """class that defines a sudoku grid"""
    def __init__(self, grid):
        """init sudoku with grid"""
        self.grid = grid
        self.backtrace = []
        self.rows = []
        self.columns = []
        self.blocks = []
        self.update()

    def updateRows(self):
        """update lines buffer"""
        self.rows = []
        for row in self.grid:
            available = list(range(1,10))
            for point in row:
                if point != 0:
                    available.remove(point)
            self.rows.append(available)
        # print(self.rows)

    def updateColumns(self):
        """update columns buffer"""
        self.columns = []
        for column in zip(*self.grid):
            available = list(range(1,10))
            for point in column:
                if point != 0:
                    available.remove(point)
            self.columns.append(available)
        # print(self.columns)

    def updateBlocks(self):
        """update columns buffer"""
        self.blocks = []
        for block in range(9):
            available = list(range(1,10))
            for point in range(9):
                point = self.grid[(block // 3) * 3 + point // 3][(block % 3) * 3 + point % 3]
                if point != 0:
                    available.remove(point)
            self.blocks.append(available)
        # print(self.blocks)

    def update(self):
        """update sudoku possibilities with grid"""
        self.updateRows()
        self.updateColumns()
        self.updateBlocks()


    def free(self, x, y):
        """return a list of available numbers for the case in position indicated
        by x and y, reurn none if already validated"""
        if self.grid[y][x] != 0:
            return []
        row = self.rows[y]
        col = self.columns[x]
        block = self.blocks[((y // 3) * 3) + (x // 3)]

        return list(set(row) & set(col) & set(block))

    def solve(self):
        """return a list of available numbers for the case in position indicated
        by x and y, reurn none if already validated"""
        keep_going = True
        while keep_going:
            keep_going = False
            for x in range(9):
                for y in range(9):
                    free = self.free(x, y)
                    print(x, y, free)
                    if len(free) == 1:
                        keep_going = True
                        self.grid[y][x] = free[0]
                        self.update()



    def print(self):
        """print on stdout the sudo ku grid as is"""


        print(os.linesep.join((''.join(((str(i) if i != 0 else '.')
            for i in row))
            for row in self.grid)))


    def solved(self):
        """True if solved, False otherwise"""
        return sum((len(row) for row in self.rows)) == 0




class SudokuParser:
    """class for parsing sudoku grids"""
    def __init__(self, filename=None, fmt=('', '', '.', '\n')):
        """init method, use filename if sent, stdin otherwise"""
        if filename is not None:
            raise Exception('filenames not yet implemented')
        self.fd = sys.stdin
        self.fmt = fmt

    def parse(self):
        """return a sudoku grid (2 sides tuple of int)"""
        for line in self.fd.readlines():
            yield [[int(c) if c != '.' else 0 for c in
                line[i:i+9]] for i in range(0, 81, 9)]


# grid = (
#         (1,2,3, 4,5,6, 7,8,9),
#         (4,5,6, 7,8,9, 1,2,3),
#         (7,8,9, 1,2,3, 4,5,6),
#
#         (2,3,4, 5,6,7, 8,9,1),
#         (5,6,7, 8,9,1, 2,3,4),
#         (8,9,1, 2,3,4, 5,6,7),
#
#         (3,4,5, 6,7,8, 9,1,2),
#         (6,7,8, 9,1,2, 3,4,5),
#         (9,1,2, 3,4,5, 6,7,8),
#         )

for grid in SudokuParser().parse():
    sudoku = Sudoku(grid)
    #sudoku.print()
    #print()
    sudoku.solve()
    if sudoku.solved():
        sudoku.print()


