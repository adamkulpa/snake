# -*- coding: utf-8 -*-

"""
Created on 30 Jul. 2016

@file: Timer.py
@brief: This file contain simple wrapper for pygame.timer module with extended
        functionality: stop and pause.
@autor: Adam Kulpa
"""


import pygame


class Timer:
    def __init__(self):
        self._start_ticks = 0
        self._paused_ticks = 0
        self._paused = False
        self._started = False
        
    def start(self):
        self._paused = False
        self._started = True
        self._start_ticks = pygame.time.get_ticks()
        
    def stop(self):
        self._paused = False
        self._started = False
        
    def get_ticks(self):
        if self._started:
            if self._paused:
                return self._paused_ticks
            else:
                return pygame.time.get_ticks() - self._start_ticks
        else:
            return 0
    
    def pause(self):
        if self._started and not self._paused:
            self._paused = True
            self._paused_ticks = pygame.time.get_ticks() - self._start_ticks
    
    def unpause(self):
        if self._paused:
            self._paused = False
            self._start_ticks = pygame.time.get_ticks() - self._paused_ticks
            self._paused_ticks = 0
            
    def is_started(self):
        return self._started
    
    def is_paused(self):
        return self._paused
