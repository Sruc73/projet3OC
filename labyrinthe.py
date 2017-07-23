#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk
from random import randint




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
        self.ligne = rows
        self.colonnes = cols

    # Return a tuple (x, y) with x = row number and y = col number
    def random_position(self, a, b):
        self.x = randint(a, b)
        self.y = randint(a,b)
        return (self.x, self.y)

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
        # Add 1 to character's position (line) if right arrow is pressed
        # Remove 1 to character's position (line) if left arrow is pressed
        # Add 1 to character's position (column) if top arrow is pressed
        # Remove 1 to charater's position (column) if bottom arrow is pressed
        pass


def main():
    lab = Grid()
    print(lab.tab)
    agent = Position(3, 8)
    print(agent.random_position(0, 6))
    print(agent)



if __name__ == "__main__":
    main()
