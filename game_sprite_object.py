import pygame
from game_object import GameObject


class GameSpriteObject(pygame.sprite.Sprite, GameObject):

    def __init__(self, settings, screen):
        pygame.sprite.Sprite.__init__(self)
        GameObject.__init__(self, settings, screen)
