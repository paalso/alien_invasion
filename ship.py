import pygame
from game_object import GameObject


class Ship(GameObject):
    def __init__(self, settings, screen):

        super().__init__(settings, screen)

        self.image = pygame.transform.scale(
                pygame.image.load(settings.ship_img),
                (self.settings.ship_width, self.settings.ship_height))
        self.rect = self.image.get_rect()

        self.rect.bottom = self.sc_rect.bottom
        self.set_center()

        self.moving_left = False
        self.moving_right = False

    def handle_keydown(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = True
        if key == pygame.K_RIGHT:
            self.moving_right = True

    def handle_keyup(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = False
        if key == pygame.K_RIGHT:
            self.moving_right = False

    def update(self):
        shift = self.settings.ship_speed
        if self.moving_right and self.right < self.sc_rect.right:
            self.move(shift, 0)
        if self.moving_left and self.left > self.sc_rect.left:
            self.move(-shift, 0)

    def set_center(self):
        self.rect.centerx = self.sc_rect.centerx
