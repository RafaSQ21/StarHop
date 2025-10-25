#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from Model.Const import WIN_WIDTH, COLOR_YELLOW, MENU_OPTION, COLOR_WHITE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./Asset/Menu.png')
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self, ):
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            self.menu_text(35, "Star Houp", COLOR_YELLOW, ((WIN_WIDTH / 2), 70))

            for i in range(len(MENU_OPTION)):
                self.menu_text(20, MENU_OPTION[i], COLOR_WHITE, ((WIN_WIDTH / 2), 120 + 25 * i))

            pygame.display.flip()
            # por while e inverter a musica com imagem
            # pygame.mixer_music.load('./asset/Menu.mp3')
            # pygame.mixer_music.play(-1)

            # Checar os eventos

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name='Lucida Sans Typewriter', size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()  # fechar janela
                quit()  # Fim pygame
