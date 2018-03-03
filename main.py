#! /usr/bin/python
# -*- coding: utf-8 -*-

"""
Created on 29 Jul. 2016

@file: main.py
@brief: It's small, well-know game realization called 'Snake'. 
        The only purpos of Snake is to chase after food blocks
        to feed and get longer.
@autor: Adam Kulpa
"""


from Application import App


def main():
    app = App()
    app.on_execute()


if __name__ == "__main__":
    main()
