import pygame
from game.game_object import GameObject

class GameRectObject(GameObject):

    counter = 0

    def __init__(self, settings, screen, x, y, w, h):
        super().__init__(settings, screen)
        self.surface = pygame.Surface((w, h))
        self.rect = pygame.Rect(x, y, w, h)

    def draw(self):
        self.screen.blit(self.surface, self.rect)
