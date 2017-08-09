#! /usr/bin/env python3
# coding: utf-8

import pygame
from random import choice, randint



class Grid:

    ROWS = 14
    COLS = 14

    def __init__(self, struct):
        """Constructor for a 15X15 grid"""
        self.file = struct
        self.structure = 0

    # def build_lab(self):
    #     """Method to create a level thanks to file structure.txt"""
	# 	#Open file
	# 	with open(self.file, "r") as struct_file:
    #         level_struct = []
	# 		#lines of the file
	# 		for line in struct_file:
	# 			level_line = []
	# 			#sprites in file
	# 			for sprite in line:
	# 				#ignore "\n"
	# 				if sprite != '\n':
	# 					# Add sprite to the line
	# 					level_line.append(sprite)
	# 			# Add the line to the level structure
	# 			level_struct.append(level_line)
	# 		# Save the structure
	# 		self.structure = level_struct

        def display_lab(self):
            """Diplay the labyrinthe with structure send by method build_lab"""
            #Pictures
            wall = "data/wall.jpg"
            floor = "data/floor.jpg"


        def empty_boxes(self):
            """ Added empty boxes from level_struct in list empty_b"""
            empty_b = [(i, j) for i in range(0, len(ROWS)) \
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
        # Seconde solution en tirant au sort dans la liste empty_boxes
        # rand_position = choice(empty_boxes)
        # # Je supprime de la liste empty_boxes la valeur tirée au sort au-dessus
        # for i in empty_boxes:
        #     if i == rand_position:
        #         empty_boxes.remove(rand_position)
        # # J'affecte chaque valeur du tuple à rand_x et rand_y
        # rand_x = rand_position[0]
        # rand_y = rand_position[1]
        # return (rand_x, rand_y)

    def put_in_lab(self, position):
        pass




class Character():

    def __init__(self):
        self.name = name
        self.picture = "data/macgyver.png"

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
                    if self.structure[self.case_x][self.case_y] != "#":
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


class Lab_keeper(Character):

    """ Create a keeper with a fixed position """
    def __init__(self):
        self.name = "Murdoc"
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

# pygame.init()
#
# NUMBER_OF_SPRITE = 15 # There's 15 sprite per line
# SPRITE_SIZE = 30 # 1 sprite = 30 pixels
#
# SIZE = NUMBER_OF_SPRITE * SPRITE_SIZE
# # Created the window for game
# size = pygame.display.set_mode(size)

# Déplacement madgyver
# if event.key == K_RIGHT:
#    macgyver.move_character("right")
# elif event.key == K_LEFT:
#   macgyver.move_character("left")
# elif event.key == K_DOWN:
#   macgyver.move_character("down")
# elif event.key == K_UP:
#   macgyver.move_character("up")


def main():
    lab = Grid()
    keeper = Lab_keeper()
    print(Lab_keeper.name)
    print(Lab_keeper.position)
    perso1 = MacGyver()
    print(perso1.name)
    print(perso1.position)
    perso1.put_in_lab(perso1.position)
    aiguille = Objects("aiguille")
    print(aiguille.name)
    print(aiguille.position)


if __name__ == "__main__":
    main()
