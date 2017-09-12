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
        # Open file
        with open(self.file, "r") as f:
                        # lines of the file
            for index, line in enumerate(f):
                level_line = []
                #sprites in file
                for sprite in line:
                    # ignore "\n"
                    if sprite != '\n':
                        # Add sprite to the line
                        level_line.append(sprite)
                    # Get number of signs to get number of columns
                    if index == 0:
                        Grid.COLS = len(line) - 1
                Grid.ROWS += 1
                # Add the line to the level structure
                self.LEVEL_STRUCT.append(level_line)

    def display_lab(self, screen):
        """Display the labyrinth with structure send by method build_lab"""
        wall = load_image("wall.jpg")

        line_number = 0
        for line in self.LEVEL_STRUCT:
            sprite_number = 0
            for sprite in line:
                # sprite's position in pixels (1 sprite = 30 px)
                x = sprite_number * 30
                y = line_number * 30

                if sprite == "#":
                    screen.blit(wall, (x, y))
                elif sprite == mcGyver:
                    screen.blit(mcGyver.picture, mcGyver.p_rect)
                elif sprite == keeper:
                    screen.blit(keeper.picture, keeper.rect)
                elif sprite == ether:
                    screen.blit(ether.picture, ether.rect)
                elif sprite == syringe:
                    screen.blit(syringe.picture, syringe.rect)
                elif sprite == needle:
                    screen.blit(needle.picture, needle.rect)
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

    def wall_position():
        """ Return a tuple's list for wall position"""

        walls = [(i, j) for i in range(Grid.ROWS)
                 for j in range(Grid.COLS) if Grid.LEVEL_STRUCT[i][j] == "#"]
        return walls


class Character():

    def __init__(self, name, picture):
        self.name = name
        self.picture = load_image(picture)
        # Put picture's size at 30 X 30 pixels
        self.picture = pg.transform.scale(self.picture, (30, 30))

        # screen.blit(self.picture, self.picture_rect)


class MacGyver(Character):

    """Create the character MacGyver with a random position
        when the game start"""

    def __init__(self, name, picture):
        super().__init__(name, picture)
        self.position = Position.random_position()
        self.p_rect = self.picture.get_rect()
        self.p_rect = pg.Rect(self.position[1] * 30, self.position[0] * 30, 30, 30)
        self.x = 30
        self.y = 30


class LabKeeper(Character):

    """Create a keeper with a fixed position"""

    def __init__(self, name, picture):
        super().__init__(name, picture)
        self.position = Position.fixed_position()
        self.rect = pg.Rect(self.position[1] * 30, self.position[0] * 30, 30, 30)


class Objects():
    """Create objects(and incremente counter for each one)
    to make McGyver able to asleep Murdoc"""
    # Initialize a counter to know how many Objects's instances are created
    counter = 0

    def __init__(self, name, picture):
        self.position = Position.random_position()
        self.name = name
        self.picture = load_image(picture)
        self.rect = pg.Rect(self.position[1] * 30, self.position[0] * 30, 30, 30)
        self.counter += 1


class Wall(Objects):

    def __init__(self, name, picture):
        super().__init__(name, picture)
        self.name = name
        self.picture = load_image(picture)
        self.w_rect = self.picture.get_rect()



# ----------------------------------------------------------------------
    # Initialize and set up screen
#-----------------------------------------------------------------------
pg.init()

SIZE = 450  # 15 sprites * 30 pixels
screen = pg.display.set_mode((SIZE, SIZE))
# Window's title
pg.display.set_caption("MacGyver's labyrinth")
background = load_image("floor.png")
background = pg.transform.scale(background, (SIZE, SIZE))
screen.blit(background, (0, 0))

# Create the labyrinth
lab = Grid("structure.txt")
mcGyver = MacGyver("Mac Gyver", "macgyver.png")
keeper = LabKeeper("Murdoc", "murdoc.png")
ether = Objects("ether", "ether.png")
needle = Objects("needle", "needle.png")
syringe = Objects("syringe", "syringe.png")
# wall = Wall("wall", "wall.jpg")

# Put characters and objects in labyrinth
Grid.put_in_lab(mcGyver, keeper, ether, needle, syringe)


lab.display_lab(screen)
pg.key.set_repeat(400, 30)
pg.display.flip()


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
                mcGyver.p_rect = mcGyver.p_rect.move(mcGyver.x, 0)
                # if mcGyver.p_rect.colliderect(w_rect):
                #     mcGyver.p_rect = mcGyver.p_rect.move(mcGyver.x - 1, 0)
            elif event.key == K_LEFT:
                # if Grid.LEVEL_STRUCT[mcGyver.position[0]][mcGyver.position[1] - 1] != "#":
                mcGyver.p_rect = mcGyver.p_rect.move(-mcGyver.x, 0)
            elif event.key == K_UP:
                mcGyver.p_rect = mcGyver.p_rect.move(0, -mcGyver.y)
            elif event.key == K_DOWN:
                mcGyver.p_rect = mcGyver.p_rect.move(0, mcGyver.y)

    screen.blit(background, (0, 0))
    lab.display_lab(screen)
    screen.blit(mcGyver.picture, mcGyver.p_rect)
    pg.display.flip()

# def main():
#
#
# if __name__ == "__main__":
#     main()
