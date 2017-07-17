#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk


class Grid:

    ROWS = 15
    COLS = 15

    def __init__(self):
        """Constructor for a 15X15 grid"""
        # Filled the grid with number 1 to have a visual
        print([[1] * self.COLS for y in range(self.ROWS)])


def main():
    lab = Grid()

if __name__ == "__main__":
    main()
