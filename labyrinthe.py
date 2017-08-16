#! /usr/bin/env python3
# coding: utf-8

import pygame as pg
from pygame.locals import *
from random import choice
import os



# def load_image(name):
#     """
#         Load a picture
#     """
#     img_name = os.path.join('data', name)
#     picture = pg.image.load(img_name)
#     picture = picture.convert()
#     return picture

# def run_game():
#     # Initialize and srt up screen
#     pg.init()
#
#     # 15 sprites * 30 pixels
#     size = 15*30
#     speed = [2, 2]
#     black = (0, 0, 0)
#
#     window = pg.display.set_mode((size, size))
#     pg.display.set_caption("MacGyver's labyrinthe")
#
#     background = pg.Surface(window.get_size())
#     background = background.convert()
#     background.fill((250, 250, 250))

    # Main loop
    #
    # while True:
    #     for event in pg.event.get():
    #         # if user quit the game
    #         if event.type == pg.QUIT:
    #             sys.exit()
    #         # if esc key is pressed
    #         elif event.type == pg.KEYDOWN:
    #             if event.key == pg.K_ESCAPE:
    #                 return
    #
    #     window.blit(background, (0, 0))
    #     pg.display.flip()


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
        # empty_b = [(i, j) for i in range(0, 15) \
        # for j in range(0, 15) if cls.LEVEL_STRUCT[i][j] == "."]
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

    def display_lab(self, window):
        """Diplay the labyrinthe with structure send by method build_lab"""
        # Pictures
        mcGyver = pg.image.load('data/macgyver.png')
        murdoc = pg.image.load('data/murdoc.png')
        wall = pg.image.load('data/wall.jpg')
        floor = pg.image.load('data/floor.png')
        ether = pg.image.load('data/ether.png')

        line_number = 0
        for line in self.LEVEL_STRUCT:
            sprite_number = 0
            for sprite in line:
                # sprite's position in pixels (1 sprite = 30 px)
                x = line_number * 30
                y = sprite_number * 30
                if sprite == "#":
                    screen_surface.blit(wall, (x, y))
                elif sprite == ".":
                    window.blit(floor, (x, y))
                sprite_number += 1
            line_number += 1



class Position():
    """ Return the position in the grid """
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

    def fixed_position():
        """
            Browse the structure to find the letter k's position
            to put Murdoc in lab
        """

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
        """ Return a random tuple(x, y) with x = row number and y = col number
            to set an object in the grid """

        # Removes random value from empty_boxes list
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
        self.macgyver_picture = pg.image.load('data/macgyver.png')


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
        self.position = Position.fixed_position()
        self.keeper_picture = "data/murdoc.png"


class Objects():

    def __init__(self, name):
        self.position = Position.random_position()
        self.name = name
        #self.picture = picture

    def positionner(self):
        self.ligne = self.position[0]
        self.colonne = self.position[1]


# ----------------------------------------------------------------------
    # Initialize and set up screen
#-----------------------------------------------------------------------
pg.init()

size = 15*30
screen_surface = pg.display.set_mode((size, size))
# Window's title
pg.display.set_caption("MacGyver's labyrinthe")

lab = Grid("structure.txt")
lab.build_lab()
lab.display_lab(screen_surface)

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

    pg.display.flip()


def main():

    lab = Grid("structure.txt")
    keeper = Lab_keeper()
    print(keeper.name)
    print(keeper.position)

    perso1 = MacGyver("data/macgyver.png")
    print(perso1.name)
    print(perso1.position)

    aiguille = Objects("aiguille")
    ether = Objects("ether")
    seringue = Objects("seringue")

    print(aiguille.name)
    print(aiguille.position)

    print(ether.name)
    print(ether.position)

    print(seringue.name)
    print(seringue.position)

    Grid.put_in_lab(perso1, keeper, aiguille, ether, seringue)
    print(Grid.LEVEL_STRUCT)


if __name__ == "__main__":
    main()
