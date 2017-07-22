#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk
from Random import randint




class Grid:

    ROWS = 15
    COLS = 15
    WALL ="#"

    def __init__(self):
        """Constructor for a 15X15 grid"""
        self.tab = [[self.WALL] * self.ROWS for y in range(self.COLS)]

    # def __str__(self):
    #
    #     return str(self.lab)


class Position():
    """ Return the position in the grid """
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        return rows, cols

    # ToDo: Random pour placer aléatoirement les objets

    @property
    def rows(self):
        return self.rows

    @property
    def cols(self):
        return self.cols


class Character(Position):

    def __init__(self, Position):
        pass

    def move_character():
        pass


def main():
    lab = Grid()
    print(lab.tab)

if __name__ == "__main__":
    main()
