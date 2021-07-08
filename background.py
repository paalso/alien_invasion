import pygame
import settings
from game_object import GameObject


class Background(GameObject):

    def __init__(self, settings, screen):
        super().__init__(settings, screen)

        self.set_image(self.settings.background)

        self.rect = self.image.get_rect()

    def set_image(self, image_file):
        self.image = pygame.transform.scale(
            pygame.image.load(image_file),
            (self.settings.screen_width, self.settings.screen_height))

    def draw(self):
        self.screen.blit(self.image, (0, 0))
