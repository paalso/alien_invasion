import pygame
import settings


class Background:

    def __init__(self, ai_settings, screen):
        self.image = pygame.transform.scale(
            pygame.image.load(ai_settings.background),
            (ai_settings.screen_width, ai_settings.screen_height))
        self.screen = screen

    def draw(self):
        self.screen.blit(self.image, (0, 0))
