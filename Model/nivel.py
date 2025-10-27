#!/usr/bin/python
# -*- coding: utf-8 -*-
from idlelib.calltip import get_entity

from Model import fabricaEntidades
import pygame

from Model.entidade import Entidade
from Model.fabricaEntidades import FabricaEntidades


class Nivel:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entidade] = []
        self.entity_list.extend(FabricaEntidades.get_entidade('Nivel1IM'))

    def run(self):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()
        pass
