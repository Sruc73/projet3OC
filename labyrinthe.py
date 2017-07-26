#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk
from random import randint
import os


class Grid:

    ROWS = 15
    COLS = 15
    WALL ="#"

    def __init__(self):
        """Constructor for a 15X15 grid"""
        self.tab = [[self.WALL * self.ROWS] for y in range(self.COLS)]

    def is_free(self, a, b):
        """ Boolean to know if a box is free or not """
        for a, b in self.tab:
            if self.tab[a][b] == "#":
                return False
            else:
                return True

    # def __str__(self):
    #
    #     return str(self.lab)


class Position():
    """ Return the position in the grid """
    def __init__(self, rows, cols):
        self.ligne = rows
        self.colonnes = cols

    def random_position(self, a, b):
        """ Return a random tuple (x, y) with x = row number and y = col number
            to set an object in the grid """

        # Ajouter la gestion des cases déja occupées par un objet
        # Si la case est occupée, on choisi un autre random tuple
        self.x = randint(a, b)
        self.y = randint(a,b)
        return (self.x, self.y)

    # @property
    # def rows(self):
    #     return self.rows
    #
    # @property
    # def cols(self):
    #     return self.cols


class Character(Position):

    def __init__(self, Position):
        pass

    def move_character():
        # Add 1 to character's position (line) if right arrow is pressed
        # Remove 1 to character's position (line) if left arrow is pressed
        # Add 1 to character's position (column) if top arrow is pressed
        # Remove 1 to charater's position (column) if bottom arrow is pressed
        pass

    def get_object():
        """ Add all items picked up to make the syringe """
        pass


def main():
    lab = Grid()
    print(lab.tab)
    place = Position(0, 17)
    place.random_position(0, 17)
    print(place)
    # print(place.random_position(0, 6))
    # print(place)



if __name__ == "__main__":
    main()
