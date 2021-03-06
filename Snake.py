# -*- coding: utf-8 -*-

"""
Created on 29 Jul. 2016

@file: Snake.py
@brief: This class represents description of a snake, including shape
        and behavior.
@autor: Adam Kulpa
"""

import pygame

from Timer import Timer
from Palette import Colors


class Snake(object):
    SNAKE_DIR_NONE = -1
    SNAKE_DIR_UP = 1
    SNAKE_DIR_DOWN = 2
    SNAKE_DIR_LEFT = 3
    SNAKE_DIR_RIGHT = 4

    WIDTH, HEIGHT = 20, 20

    def __init__(self):
        self._direction = Snake.SNAKE_DIR_NONE
        self._last_direction = Snake.SNAKE_DIR_NONE
        self._length = 3
        self._part_position = [i for i in range(self._length)]
        self._speed = 100
        self._speed_timer = Timer()
        self._speed_timer.start()

    def set_position(self, x, y):
        self._part_position[0] = (x, y)
        for i in range(len(self._part_position)):
            self._part_position[i] = (x - i * self.WIDTH, y)

    def set_direction(self, snake_dir):
        transition_possible = True

        if ((self._direction == Snake.SNAKE_DIR_LEFT and
             snake_dir == Snake.SNAKE_DIR_RIGHT)):
            transition_possible = False

        if ((self._direction == Snake.SNAKE_DIR_RIGHT and
             snake_dir == Snake.SNAKE_DIR_LEFT)):
            transition_possible = False

        if ((self._direction == Snake.SNAKE_DIR_UP and
             snake_dir == Snake.SNAKE_DIR_DOWN)):
            transition_possible = False

        if ((self._direction == Snake.SNAKE_DIR_DOWN and
             snake_dir == Snake.SNAKE_DIR_UP)):
            transition_possible = False

        if transition_possible:
            self._last_direction = self._direction
            self._direction = snake_dir

    def update(self):
        if self._speed_timer.get_ticks() >= self._speed:

            if self._direction == Snake.SNAKE_DIR_NONE:
                self.move_head(0, 0)
            else:
                self.update_parts_position()

            if self._direction == Snake.SNAKE_DIR_UP:
                self.move_head(0, -Snake.HEIGHT)
            if self._direction == self.SNAKE_DIR_DOWN:
                self.move_head(0, Snake.HEIGHT)
            if self._direction == Snake.SNAKE_DIR_LEFT:
                self.move_head(-Snake.WIDTH, 0)
            if self._direction == Snake.SNAKE_DIR_RIGHT:
                self.move_head(Snake.WIDTH, 0)

            self._speed_timer.start()

    def draw(self, dest_surf):
        for i in range(len(self._part_position)):
            x, y = self._part_position[i]
            if i == 0:
                pygame.draw.rect(dest_surf, Colors['HEAD'],
                                 (x, y, Snake.WIDTH, Snake.HEIGHT))
            else:
                pygame.draw.rect(dest_surf, Colors['BODY'],
                                 (x, y, Snake.WIDTH, Snake.HEIGHT))

    def move_head(self, dx, dy):
        x, y = self._part_position[0]
        self._part_position[0] = (x + dx, y + dy)

    def update_parts_position(self):
        for i in range(len(self._part_position) - 1, 0, -1):
            self._part_position[i] = self._part_position[i - 1]
