import pygame

from game_group_object import GameGroupObject
from ship import Ship
from projectile import Projectile
from alien import Alien


class Projectiles(GameGroupObject):

    def __init__(self, settings, screen, ship, aliens):
        super().__init__(settings, screen)
        self.ship = ship
        self.aliens = aliens

        self.drop_speed_increase_factor_per_alien = \
                self.settings.drop_speed_increase_factor ** \
                (1 / aliens.number)

        self.speed_increase_factor_per_alien = \
                self.settings.alien_speed_increase_factor ** \
                (1 / aliens.number)

    def fire_projectile(self, ship):
        if len(self.items) < self.settings.projectiles_allowed:
            projectile = Projectile(self.settings, self.screen, ship)
            self.items.add(projectile)

    def handle_keydown(self, key):
        if key == pygame.K_SPACE:
            self.fire_projectile(self.ship)

    def update(self):
        super().update()
        self.__check_bullet_alien_collisions()      # aliens


    def __check_bullet_alien_collisions(self):
        for projectile in self.items.copy():
            if projectile.rect.bottom <= 0:
                self.items.remove(projectile)

            for alien in self.aliens:
                if projectile.rect.colliderect(alien.rect):

                    self.items.remove(projectile)
                    self.aliens.remove(alien)
                    self.aliens.fleet_drop_speed *= \
                            self.drop_speed_increase_factor_per_alien
                    Alien.speed_increase_factor *= \
                            self.speed_increase_factor_per_alien
                    break
