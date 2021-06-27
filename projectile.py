import pygame
from game_object import GameObject


class Projectile(GameObject, pygame.sprite.Sprite):

    def __init__(self, settings, screen, ship):
        pygame.sprite.Sprite.__init__(self)
        GameObject.__init__(self, settings, screen)

        self.ship = ship
        self.speed = (0, -settings.projectile_speed)

        self.image = pygame.transform.scale(
                pygame.image.load(
                    self.settings.projectile_img),
                    (self.settings.projectile_width,
                    self.settings.projectile_length))
        self.rect = self.image.get_rect()

        self.rect.centerx = ship.centerx
        self.rect.top = ship.top

        pygame.mixer.Sound(self.settings.projectile_launch_sound).play()
