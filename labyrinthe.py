#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk
from random import randint
import os


class Grid:

    ROWS = 15
    COLS = 15
    wall ="*" # Importer depuis le fichier structure.txt les chaines de caractere shcématisant le laby

    def __init__(self):
        """Constructor for a 15X15 grid"""
        self.tab = [[self.wall]  * self.ROWS for y in range(self.COLS)]


    def is_free(self, row, col):
        """ To know if a box is empty or not """
        for i in range(self.rows):
            if self.tab[row][col] == " ":
                return True
            else:
                return False



class Position():
    """ Return the position in the grid """
    def __init__(self, rows, cols):
        self.ligne = rows
        self.colonnes = cols

    def position_tuple(self):
        return(self.ligne, self.colonnes)


    def random_position(a, b):
        """ Return a random tuple (x, y) with x = row number and y = col number
            to set an object in the grid """
        # Ajouter la gestion des cases déja occupées par un objet
        # Si la case est occupée, on choisi un autre random tuple
        x = randint(a, b)
        y = randint(a, b)
        return (x, y)


class Character():

    def __init__(self):
        self.name = name
        self.picture = picture
        self.position = position.position_tuple()

    def move_character():
        # Add 1 to character's position (line) if right arrow is pressed
        # Remove 1 to character's position (line) if left arrow is pressed
        # Add 1 to character's position (column) if top arrow is pressed
        # Remove 1 to charater's position (column) if bottom arrow is pressed
        pass

    def get_object():
        """ Add all items picked up to make the syringe """
        pass


class MacGyver(Character):

    """ Create the character MacGyver with a random position
        when the game start """
    def __init__(self):
        self.name = "Mc Gyver"
        self.position = Position.random_position(0, 14)
        # self.picture = Add path to MacGyver's picture


class Gardien(Character):

    """ Create a keeper with a fixed position """
    def __init__(self):
        self.name = "Keeper"
        self.place = Position(14, 7) # Fixed position


class Objects():

    def __init__(self, name):
        self.position = Position.random_position(0, 14)
        self.name = name
        # self.picture = add path to Objects' picture


def main():
    lab = Grid()
    print(lab.tab)
    lab.tab[3][4] = "M"
    print(lab.tab)
    keeper = Gardien()
    print(keeper.name)
    keeper.position = keeper.name
    print(lab.tab)
    perso1 = MacGyver()
    print(perso1.name)
    print(perso1.position)
    aiguille = Objects("aiguille")
    print(aiguille.name)
    print(aiguille.position)


if __name__ == "__main__":
    main()
