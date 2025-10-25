#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from Model.menu import Menu


class Jogo:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((800, 600))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Checar os eventos
            # for event in pygame.event.get():
            #   if event.type == pygame.QUIT:
            #      pygame.quit()  # fechar janela
            #     quit()  # Fim pygame
