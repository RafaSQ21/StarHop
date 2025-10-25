#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Model.Const import WIN_HEIGHT, WIN_WIDTH
from Model.menu import Menu


class Jogo:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

