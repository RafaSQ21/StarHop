#!/usr/bin/python
# -*- coding: utf-8 -*-
from typing import Any

from Model.Const import WIN_WIDTH
from Model.imagemDeFundo import ImagemDeFundo


class FabricaEntidades:

    @staticmethod
    def get_entidade(entity_name: str, position=(0, 0)):
        match entity_name:
            case 'Nivel1IM':
                list_im = []
                for i in range(4):
                    list_im.append(ImagemDeFundo(f'Nivel1IM{i}', (0, 0)))
                    list_im.append(ImagemDeFundo(f'Nivel1IM{i}', (WIN_WIDTH, 0)))
                return list_im
