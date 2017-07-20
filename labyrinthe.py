#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk


class Grid:

    ROWS = 15
    COLS = 15
    WALL = "/"
    #
    # def __init__(self):
    #     """Constructor for a 15X15 grid"""
    #     print([[self.WALL] * self.COLS for y in range(self.ROWS)])

    # def __init__(self):
    #     """ Constructor for a 15X15 grid """
    #     print([[(row, col) for col in range(0, self.COLS)]\
    #         for row in range(0, self.ROWS)])

    def __init__(self):
        """Create a grid 15X15"""
        labyrinthe = []
        for i in range(self.ROWS):
            labyrinthe.append([])
            for j in range(self.COLS):
                labyrinthe[i].append(self.WALL)
        print(labyrinthe)


def main():
    lab = Grid()

if __name__ == "__main__":
    main()
