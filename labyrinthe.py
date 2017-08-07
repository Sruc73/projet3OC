#! /usr/bin/env python3
# coding: utf-8

import tkinter as tk
from random import randint



class Grid:

    ROWS = 15
    COLS = 15

    def __init__(self, struct_file):
        """Constructor for a 15X15 grid"""
        self.file = struct_file

    def build_lab(self):
        """Method to create a level thanks to file structure.txt"""
		#Open file
		with open(self.file, "r") as struct_file:
            level_struct = []
			#lines of the file
			for line in struct_file:
				level_line = []
				#sprites in the file
				for sprite in line:
					#ignore "\n"
					if sprite != '\n':
						# Add sprite to the line
						level_line.append(sprite)
				# Add the line to the level structure
				level_struct.append(level_line)
			# Save the structure
			self.structure = level_struct


    def is_free(self, row, col):
        """ To know if a box is empty or not """
        # for i in range(self.rows):
        #     if self.tab[row][col] == " ":
        #         return True
        #     else:
        #         return False

        # Parcourir le labyrinthe et créer un tuple pour chaque case sur laquelle
        # il n'y a pas d'objet positionné dessus les stocker dans une liste
        # et comparer les coordonnées des objets/perso aux tuples de la liste
        # afin de savoir si on peut le placer ici
        # Autrement, attribuer une nouvelle case à l'objet


class Position():
    """ Return the position in the grid """
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def fixed_position(row, col):
        fixed_rows = row
        fixed_cols = col
        return (fixed_rows, fixed_cols)

    def random_position(a, b):
        """ Return a random tuple(x, y) with x = row number and y = col number
            to set an object in the grid """
        rand_x = randint(a, b)
        rand_y = randint(a, b)
        return (rand_x, rand_y)


class Character():

    def __init__(self):
        self.name = name
        self.picture = picture
        # self.position = Position.grid_coord

    def put_character_in_lab(self):
        list[[a],[b]]

        pass


    def move_character():
        # If there's no wall:
            # Add 1 to character's position (line) if right arrow is pressed
            # Remove 1 to character's position (line) if left arrow is pressed
            # Add 1 to character's position (column) if top arrow is pressed
            # Remove 1 to charater's position (column) if bottom arrow is pressed
        # Else:
            # character doesn't move
        pass

    def get_object():
        """ Add all items picked up to make the syringe """
        pass


class MacGyver(Character):

    """ Create the character MacGyver with a random position
        when the game start """
    def __init__(self, picture):
        self.name = "Mc Gyver"
        self.position = Position.random_position(0, 14)
        self.macgyver_picture = "data/macgyver.png"


class Keeper(Character):

    """ Create a keeper with a fixed position """
    def __init__(self):
        self.name = "Keeper"
        self.position = Position.fixed_position(14, 7)
        self.keeper_picture = "data/murdoc.png"


class Objects():

    def __init__(self, name):
        self.position = Position.random_position(0, 14)
        self.name = name
        # self.picture = add path to Objects' picture

    def positionner(self):
        self.ligne = self.position[0]
        self.colonne = self.position[1]



def main():
    lab = Grid()
    lab.build_lab(structure.txt)
    keeper = Keeper()
    print(keeper.name)
    print(keeper.position)
    perso1 = MacGyver()
    print(perso1.name)
    print(perso1.position)
    aiguille = Objects("aiguille")
    print(aiguille.name)
    print(aiguille.position)


if __name__ == "__main__":
    main()
