#! /usr/bin/env python3
# coding: utf-8

import pygame
from random import randint



class Grid:

    ROWS = 15
    COLS = 15

    def __init__(self, struct):
        """Constructor for a 15X15 grid"""
        self.file = struct
        self.structure = 0

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

        def display_lab(self):
            """Diplay the labyrinthe with structure send by method build_lab"""
            #Pictures
            wall = "data/wall.jpg"
            floor = "data/floor.jpg"


        def empty_boxes(self):
            """ Added empty boxes from level_struct in list empty_b"""
            empty_b = [(i, j) for i in range(0, len(level_struct)) \
            for j in range(0, COLS) if level_struct[i][j] == " "]


class Position():
    """ Return the position in the grid """
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def fixed_position(row, col):
        #Voir pour mettre un a (pour arrivée) dans la structure du labyrinthe
        #afin de pouvoir placer Murdoc en position fixe à cet endroit
        #en cas de nouveaux niveaux
        #Dans ce cas:

        #return [(i, j) for i in range(O, len(level_struct)) \
        # for j in range(0, COLS) if level_struct[i][j] == "a"]
        fixed_rows = row
        fixed_cols = col
        return (fixed_rows, fixed_cols)

    def random_position(a, b):
        """ Return a random tuple(x, y) with x = row number and y = col number
            to set an object in the grid """
        # Ajouter le controle que la case soit bien libre
        rand_x = randint(a, b)
        rand_y = randint(a, b)
        return (rand_x, rand_y)


class Character():

    def __init__(self):
        self.name = name
        self.picture = picture
        # self.position = Position.grid_coord

    def put_character_in_lab(self, position):
        self.case_x = position[0]
        self.case_y = position[1]

        pass


    def move_character(self, direction):
        # If there's no wall:
        # Add 1 to character's position (line) if right arrow
        if direction == "right":
            if self.case_x < ROWS:
                if self.structure[self.case_x][self.case_y] != "#":
                    # Move to the right
                    self.case_x += 1
        # Remove 1 to character's position (line) if left arrow is pressed
        if direction == "left":
            if self.case_x > 0:
                if self.structure[self.case_x][self.case_y] != "#":
                    # Move to the left
                    self.case_x -= 1
            # Add 1 to character's position (column) if top arrow is pressed
            if direction == "up":
                if self.case_y > 0:
                    if self.structure[self.case_x][self.case_y] != "#"
                        self.case_y += 1
            # Remove 1 to charater's position (column) if bottom arrow pressed
            if direction == "down":
                if self.case_y < COLS:
                    if self.structure[self.case_x][self.case_y] != "#":
                        self.case_y -= 1

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
