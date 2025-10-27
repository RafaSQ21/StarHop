#!/usr/bin/python
# -*- coding: utf-8 -*-
from Model.Const import WIN_WIDTH, ENTITY_SPEED
from Model.entidade import Entidade


class ImagemDeFundo(Entidade):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED [self.name]
        if self.rect.right <=0:
            self.rect.left = WIN_WIDTH
