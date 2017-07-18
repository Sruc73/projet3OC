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
    #     # Filled the grid with number 1 to have a visual
    #     print([[1] * self.COLS for y in range(self.ROWS)])
    #
    # def __init__(self):
    #     """ Constructor for a 15X15 grid """
    #     print([[(row, col) for col in range(0, self.COLS)]\
    #         for row in range(0, self.ROWS)])

    def __init__(self):
        """Génère un plateau de jeu de taille donnée."""
        plateau = []
        for i in range(self.ROWS):
            plateau.append([])
            for j in range(self.COLS):
                plateau[i].append(self.WALL)
        print(plateau)


def main():
    lab = Grid()

if __name__ == "__main__":
    main()
