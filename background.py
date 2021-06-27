import pygame
import settings
from game_object import GameObject


class Background(GameObject):

    def __init__(self, settings, screen):
        super().__init__(settings, screen)

        self.image = pygame.transform.scale(
            pygame.image.load(settings.background),
            (settings.screen_width, settings.screen_height))
        self.rect = self.image.get_rect()

    def draw(self):
        self.screen.blit(self.image, (0, 0))
