#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from Model.Const import WIN_HEIGHT, WIN_WIDTH, MENU_OPTION
from Model.menu import Menu
from Model.nivel import Nivel


class Jogo:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                nivel = Nivel(self.window, 'Nivel1', menu_return)
                Nivel_return = nivel.run()

            elif menu_return == MENU_OPTION[3]:
                pygame.quit()
                quit()
            else:
                pass
