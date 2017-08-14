#! /usr/bin/env python3
# coding: utf-8

import pygame as pg
from random import choice



class Grid:

    ROWS = 0
    COLS = 0
    LEVEL_STRUCT = []

    def __init__(self, struct):
        """Constructor for a 15X15 grid"""
        self.file = struct
        self.structure = self.build_lab()

    @classmethod
    def put_in_lab(cls, *list_obj):
        for obj in list_obj:
            x = obj.position[0]
            y = obj.position[1]
            cls.LEVEL_STRUCT[x][y] = obj

    @classmethod
    def empty_boxes(cls):
        """ Added empty boxes from level_struct in list empty_b """
        empty_b = []
        for i in range(cls.ROWS):
            for j in range(cls.COLS):
                if cls.LEVEL_STRUCT[i][j] == ".":
                    empty_b.append((i, j))
        # empty_b = [(i, j) for i in range(0, cls.ROWS - 1) \
        # for j in range(0, cls.COLS - 1) if cls.LEVEL_STRUCT[i][j] == "."]
        return empty_b



    def build_lab(self):
        """Method to create a level thanks to file structure.txt"""
		#Open file
        with open(self.file, "r") as struct_file:
			#lines of the file
            for index, line in enumerate(struct_file):
                level_line = []
				#sprites in file
                for sprite in line:
					#ignore "\n"
                    if sprite != '\n':
						# Add sprite to the line
                        level_line.append(sprite)
                    # Get number of signs to get number of columns
                    if index == 0:
                        Grid.COLS = len(line) -1
                Grid.ROWS += 1
				# Add the line to the level structure
                self.LEVEL_STRUCT.append(level_line)

        def display_lab(self):
            """Diplay the labyrinthe with structure send by method build_lab"""
            #Pictures
            wall = "data/wall.jpg"
            floor = "data/floor.jpg"


class Position():
    """ Return the position in the grid """
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def fixed_position(x, y):
        # parcourir la structure pour trouver la position de la lettre k
        # afin d'y mettre murdoc
        x = x
        y = y
        return (x, y)

    def random_position():
        """ Return a random tuple(x, y) with x = row number and y = col number
            to set an object in the grid """
        # Ajouter le controle que la case soit bien libre
        # rand_x = randint(a, b)
        # rand_y = randint(a, b)
        # return (rand_x, rand_y)
        # Seconde solution en tirant au sort dans la liste empty_boxes

        # Je supprime de la liste empty_boxes la valeur tirée au sort au-dessus
        empty_boxes = Grid.empty_boxes()
        rand_position = choice(empty_boxes)
        for i in empty_boxes:
            if i == rand_position:
                empty_boxes.remove(rand_position)
        # Set tuple values to rand_x and rand_y
        rand_x = rand_position[0]
        rand_y = rand_position[1]
        return (rand_x, rand_y)


class Character():

    def __init__(self, name, picture):
        self.name = name
        self.picture = picture

    def get_object():
        """ Add all items picked up to make the syringe """
        pass


class MacGyver(Character):

    """ Create the character MacGyver with a random position
        when the game start """
    def __init__(self, picture):
        self.name = "Mc Gyver"
        self.position = Position.random_position()
        self.macgyver_picture = "data/macgyver.png"


    def move_character(self, direction):
        """ This method allows to move the character """
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


class Lab_keeper(Character):

    """ Create a keeper with a fixed position """
    def __init__(self):
        self.name = "Murdoc"
        self.position = Position.fixed_position(13, 14)
        self.keeper_picture = "data/murdoc.png"


class Objects():

    def __init__(self, name):
        self.position = Position.random_position()
        self.name = name
        #self.picture = picture

    def positionner(self):
        self.ligne = self.position[0]
        self.colonne = self.position[1]


# pg.init()
#
# NUMBER_OF_SPRITE = 15 # There's 15 sprites/line
# SPRITE_SIZE = 30 # 1 sprite = 30 pixels
#
# SIZE = NUMBER_OF_SPRITE * SPRITE_SIZE
# # Created the window for game
# size = pg.display.set_mode(size)

# Déplacement madgyver
# if right arrow pressed
# if event.key == K_RIGHT:
#    macgyver.move_character("right")
# else if left arrow pressed
# elif event.key == K_LEFT:
#   macgyver.move_character("left")
# else if down arrow pressed
# elif event.key == K_DOWN:
#   macgyver.move_character("down")
# else if up arrow pressed
# elif event.key == K_UP:
#   macgyver.move_character("up")


def main():
    lab = Grid("structure.txt")
    keeper = Lab_keeper()
    print(keeper.name)
    print(keeper.position)

    perso1 = MacGyver("data/macgyver.png")
    print(perso1.name)
    print(perso1.position)

    aiguille = Objects("aiguille")

    print(aiguille.name)
    print(aiguille.position)
    Grid.put_in_lab(perso1, keeper, aiguille)
    print(Grid.LEVEL_STRUCT)


if __name__ == "__main__":
    main()
