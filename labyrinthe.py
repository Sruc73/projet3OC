#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk


class Grid:

    ROWS = 15
    COLS = 15
    WALL = "/"

    def __init__(self):
        """Constructor for a 15X15 grid"""
        self.tab = [[self.WALL] * self.COLS for y in range(self.ROWS)]

    def __str__(self):
        # Pour longueur de la ligne < ROWS:



class Position():

    def __init__(self, x, y):
        for x in tab:
            pass


class Character():

    def __init__(self, Position):
        pass

def main():
    lab = Grid()
    print(lab.tab)

if __name__ == "__main__":
    main()
