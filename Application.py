# -*- coding: utf-8 -*-

"""
Created on 29 Jul. 2016

@file: Application.py
@brief: Application contains the main loop,  where all events are processed
        and dispatched. It also handles the application's initialization
        and finalization.
@autor: Adam Kulpa
"""


import sys
import pygame

from Game import Game
from Snake import Snake
from Palette import Colors


class App(object):
    def __init__(self):
        self._running = False
        self._main_clock = pygame.time.Clock()
        self._display_surf = None
        self.size = self.width, self.height = 640, 480
        self._game = Game()
        self._snake = Snake()
        self._snake.set_position(100, 100)

    def on_init(self):
        pygame.init()
        
        self._display_surf = pygame.display.set_mode(
                                self.size,
                                pygame.HWSURFACE | pygame.DOUBLEBUF)
        
        pygame.display.set_caption('Snake')

        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self._snake.set_direction(Snake.SNAKE_DIR_LEFT)
            if event.key == pygame.K_RIGHT:
                self._snake.set_direction(Snake.SNAKE_DIR_RIGHT)
            if event.key == pygame.K_UP:
                self._snake.set_direction(Snake.SNAKE_DIR_UP)
            if event.key == pygame.K_DOWN:
                self._snake.set_direction(Snake.SNAKE_DIR_DOWN)
            if event.key == pygame.K_SPACE:
                self._snake.set_direction(Snake.SNAKE_DIR_NONE)

    def on_cleanup(self):
        pygame.quit()
        sys.exit()

    def on_loop(self):
        """
        Calculations and objects update
        """
        self._snake.update()     
    
    def on_draw(self):
        """
        Draw all objects
        """
        self._display_surf.fill(Colors['BACKGROUND'])
        
        self._snake.draw(self._display_surf)
    
    def on_execute(self):
        self.on_init()
  
        """
        Main loop
        """
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)

            self.on_loop()
            
            self.on_draw()
            
            pygame.display.flip()
            
            self._main_clock.tick(60)
        
        self.on_cleanup()
