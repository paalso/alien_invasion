import pygame
from game_object import GameObject


class Alien(GameObject, pygame.sprite.Sprite):

    fleet_direction = 1   # to the right by default
    speed_increase_factor = 1

    def __init__(self, settings, screen):
        pygame.sprite.Sprite.__init__(self)
        GameObject.__init__(self, settings, screen)

        self.sc_rect = self.screen.get_rect()

        self.image = pygame.transform.scale(
                pygame.image.load(settings.alien_ship_img),
                (self.settings.alien_ship_width,
                self.settings.alien_ship_height))

        # FIX IT! : load or create true png with transparent background
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = self.settings.alien_ship_width
        self.rect.y = self.settings.alien_ship_height
        print(Alien.counter)

    def update(self):
        self.rect.x += Alien.fleet_direction * Alien.speed_increase_factor * \
                self.settings.alien_speed

    def draw(self): # или blitme?
        self.screen.blit(self.image, self.rect)

    def detect_screen_collision(self):
        return self.rect.right >= self.sc_rect.right or \
                self.rect.left <= self.sc_rect.left
