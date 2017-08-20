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
    picture = picture.convert_alpha()
    return picture


class Grid:
    """Create a grid"""

    ROWS = 0
    COLS = 0
    LEVEL_STRUCT = []

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
                    screen_surface.blit(wall, (x, y))
                elif sprite == ".":
                    window.blit(floor, (x, y))
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


class MacGyver(Character):

    """Create the character MacGyver with a random position
        when the game start"""

    def __init__(self, name, picture):
        super().__init__(name, picture)
        self.position = Position.random_position()

    def move_character(self, direction):
        """Move the character in lab"""
    # def move_character(self, direction):
    #     """ This method allows to move the character """
        # If there's no wall:
        # Add 1 to character's position (line) if right arrow
        # if direction == "right":
        #     if self.case_x < ROWS and self.structure[self.case_x][self.case_y] != "#":
        #             # Move to the right
        #             self.case_x += 1
        # # Remove 1 to character's position (line) if left arrow is pressed
        # if direction == "left" and self.case_x > 0:
        #         if self.structure[self.case_x][self.case_y] != "#":
        #             # Move to the left
        #             self.case_x -= 1
        # # Add 1 to character's position (column) if top arrow is pressed
        # if direction == "up" and self.case_y > 0:
        #         if self.structure[self.case_x][self.case_y] != "#":
        #             self.case_y += 1
        # # Remove 1 to charater's position (column) if bottom arrow pressed
        # if direction == "down" and self.case_y < COLS:
        #         if self.structure[self.case_x][self.case_y] != "#":
        #             self.case_y -= 1
        pass

    def collect_objects(self):
        pass

class Lab_keeper(Character):

    """Create a keeper with a fixed position"""
    def __init__(self, name, picture):
        super().__init__(name, picture)
        self.position = Position.fixed_position()


class Objects():
    """Create objects(and incremente counter for each one)
    to make McGyver able to asleep Murdoc"""
    #Initialize a counter to know how many Objects's instances there is
    COUNTER = 0

    def __init__(self, name, picture):
        self.position = Position.random_position()
        self.name = name
        self.picture = load_image(picture)
        Objects.COUNTER += 1

    # Créer un compteur qui compte le nombre d'objets créés
    # afin de comparer ce compteur avec le nb d'ojets récoltés
    # par mcGyver



# ----------------------------------------------------------------------
    # Initialize and set up screen
#-----------------------------------------------------------------------
pg.init()

SIZE = 15*30
screen_surface = pg.display.set_mode((SIZE, SIZE))
# Window's title
pg.display.set_caption("MacGyver's labyrinth")

# Create the labyrinth
lab = Grid("structure.txt")
mcGyver = MacGyver("Mc Gyver", "macgyver.png")
keeper = Lab_keeper("Murdoc", "murdoc.png")
ether = Objects("ether", "ether.png")
needle = Objects("needle", "needle.png")
syringe = Objects("syringe", "syringe.png")

Grid.put_in_lab(mcGyver, keeper, ether, needle, syringe)
lab.build_lab()
lab.display_lab(screen_surface)


keeper = Lab_keeper

#-----------------------------------------------------------------------
# INFINITE LOOP
#-----------------------------------------------------------------------

continue_game = True
while continue_game:
    for event in pg.event.get():
        if event.type == QUIT:
            continue_game = False
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT:
                mcGyver.move_character("right")
            elif event.key == K_LEFT:
                mcGyver.move_character("left")
            elif event.key == K_UP:
                mcGyver.move_character("up")
            elif event.key == K_DOWN:
                mcGyver.move_character("down")

    #screen_surface.blit(mcGyver.macgyver_picture)
    pg.display.flip()


# def main():

# if __name__ == "__main__":
#     main()
