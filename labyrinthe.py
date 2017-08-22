"""Openclassrooms DA Python's project 3
MacGyver's Labyrinth
MacGyver have to collect all the objects to be able to
asleep the guard
"""
#! /usr/bin/env python3
# coding: utf-8

from random import choice
import os
import pygame as pg
from pygame.locals import *

def load_image(name):
    """Load a picture with pygame"""
    img_name = os.path.join('data', name)
    picture = pg.image.load(img_name)
    picture = picture.convert()
    return picture


class Grid:
    """Create a grid"""

    LEVEL_STRUCT = []
    ROWS = 0
    COLS = 0

    def __init__(self, struct):
        """Constructor for a 15X15 grid"""
        self.file = struct
        self.structure = self.build_lab()

    @classmethod
    def put_in_lab(cls, *list_obj):
        """Put objects passed in parameter in the labyrinth"""
        for obj in list_obj:
            x = obj.position[0]
            y = obj.position[1]
            cls.LEVEL_STRUCT[x][y] = obj

    @classmethod
    def empty_boxes(cls):
        """Added empty boxes from level_struct in list empty_b"""
        empty_b = []
        for i in range(cls.ROWS):
            for j in range(cls.COLS):
                if cls.LEVEL_STRUCT[i][j] == ".":
                    empty_b.append((i, j))
        return empty_b

    def build_lab(self):
        """Method to create a labyrinth thanks to file structure.txt"""
		#Open file
        with open(self.file, "r") as f:
			#lines of the file
            for index, line in enumerate(f):
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

    def display_lab(self, window):
        """Display the labyrinthe with structure send by method build_lab"""
        # map's pictures
        wall = pg.image.load('data/wall.jpg')
        floor = pg.image.load('data/floor.png')

        line_number = 0
        for line in self.LEVEL_STRUCT:
            sprite_number = 0
            for sprite in line:
                # sprite's position in pixels (1 sprite = 30 px)
                x = sprite_number * 30
                y = line_number * 30

                if sprite == "#":
                    window.blit(wall, (x, y))
                # elif sprite == ".":
                #     screen.blit(floor, (x, y))
                elif sprite == mcGyver:
                    window.blit(mcGyver.picture, (x, y))
                elif sprite == keeper:
                    window.blit(keeper.picture, (x, y))
                elif sprite == ether:
                    window.blit(ether.picture, (x, y))
                elif sprite == syringe:
                    window.blit(syringe.picture, (x, y))
                elif sprite == needle:
                    window.blit(needle.picture, (x, y))
                sprite_number += 1
            line_number += 1


class Position():
    """Return the position in the grid"""
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def fixed_position():
        """Browse the structure to find the letter k's position
        to put Murdoc in lab"""

        lab_exit = []
        for i in range(Grid.ROWS):
            for j in range(Grid.COLS):
                if Grid.LEVEL_STRUCT[i][j] == "k":
                    lab_exit.append((i, j))
        # Set tuple's values to fixed_x and fixed_y
        fixed_x = lab_exit[0][0]
        fixed_y = lab_exit[0][1]
        return(fixed_x, fixed_y)

    def random_position():
        """Return a random tuple(x, y) with x = row number and y = col number
            to set an object in the grid"""

        # Select a value in empty_boxes and removes it from the list
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
        self.picture = load_image(picture)
        #Put picture's size at 30 X 30 pixels
        #Voir pour modifier avec utilisation de rect
        self.picture = pg.transform.scale(self.picture,(30, 30))


class MacGyver(Character):

    """Create the character MacGyver with a random position
        when the game start"""

    def __init__(self, name, picture):
        super().__init__(name, picture)
        self.position = Position.random_position()


    # def move_character(self, key):
    #     """ This method allows to move the character """
    #     if (key == K_RIGHT):
    #         #If there's no wall
    #         if self.structure[self.rand_x][self.rand_y] != "#" and self.rand_x < rows:
    #             #Move to the right
    #             self.rand_x += 1
    #     elif (key == K_LEFT):
    #         if self.structure[self.rand_x][self.rand_y] != "#" and self.rand_x > 0:
    #             #Move left
    #             self.rand_x -= 1
    #     elif (key == K_DOWN):
    #         if self.structure[self.rand_x][self.rand_y] != "#" and self.rand_y < cols:
    #             self.rand_y -= 1
    #     elif (key == K_UP):
    #         if self.structure[self.rand_x][self.rand_y] != "#" and self.rand_y > 0:
    #             self.rand_y += 1


class Lab_keeper(Character):

    """Create a keeper with a fixed position"""
    def __init__(self, name, picture):
        super().__init__(name, picture)
        self.position = Position.fixed_position()


class Objects():
    """Create objects(and incremente counter for each one)
    to make McGyver able to asleep Murdoc"""
    #Initialize a counter to know how many Objects's instances are created
    counter = 0

    def __init__(self, name, picture):
        self.position = Position.random_position()
        self.name = name
        self.picture = load_image(picture)
        self.counter += 1


# class MgGame():
#     """This class initialize a screen and create the game"""
#
#     def __init__(self, width = 15 * 30, height = 15 * 30):
#         self.width = width
#         self.height = height
#         """Initialize pygame"""
#         pg.init()
#         """Create the screen"""
#         screen_surface = pg.display.set_mode((self.width, self.height))
#         """Name the screen"""
#         pg.display.set_caption("MacGyver's labyrinth")
#
#     def main_loop(self):
#         continue_game = True
#         """Game's infinite loop"""
#         while continue_game:
#             for event in pg.event.get():
#                 if event.type == pg.QUIT:
#                     continue_game = False
#                 elif event.type == KEYDOWN:
#                     if (event.key == K_RIGHT or event.key == K_LEFT or\
#                     event.key == K_UP or event.key == K_DOWN):
#                         mcGyver.move_character(event.key)

# ----------------------------------------------------------------------
    # Initialize and set up screen
#-----------------------------------------------------------------------
pg.init()

SIZE = 450 #15 sprites * 30 pixels
screen = pg.display.set_mode((SIZE, SIZE))
background = load_image("floor.png")
background2 = pg.transform.scale(background,(SIZE,SIZE))
screen.blit(background2, (0, 0))
# Window's title
pg.display.set_caption("MacGyver's labyrinth")

# Create the labyrinth
lab = Grid("structure.txt")
mcGyver = MacGyver("Mc Gyver", "macgyver.png")
keeper = Lab_keeper("Murdoc", "murdoc.png")
ether = Objects("ether", "ether.png")
needle = Objects("needle", "needle.png")
syringe = Objects("syringe", "syringe.png")

#Put characters and objects in labyrinth
Grid.put_in_lab(mcGyver, keeper, ether, needle, syringe)
lab.display_lab(screen)


#-----------------------------------------------------------------------
# INFINITE LOOP
#-----------------------------------------------------------------------

continue_game = True
while continue_game:
    for event in pg.event.get():
        if event.type == QUIT:
            continue_game = False
        elif event.type == KEYDOWN:
            if ((event.key == K_RIGHT) or (event.key == K_LEFT)\
            or (event.key == K_UP) or (event.key == K_DOWN)):
                mcGyver.move_character(event.key)

    #screen_surface.blit(mcGyver.macgyver_picture)
    #Refreshing the screen
    pg.display.flip()

# def main():
#
#
# if __name__ == "__main__":
#     main()
