import pygame

from game_group_object import GameGroupObject
from ship import Ship
from projectile import Projectile
from alien import Alien


class Projectiles(GameGroupObject):

    def __init__(self, settings, screen, ship, aliens, game):
        super().__init__(settings, screen)
        self.ship = ship
        self.aliens = aliens
        self.game = game
        self.shots = 0

    def fire_projectile(self, ship):
        if not self.game.state == "game":
            return
        if len(self.items) < self.settings.projectiles_allowed:
            projectile = Projectile(self.settings, self.screen, ship)
            self.items.add(projectile)
            self.shots += 1

    def handle_keydown(self, key):
        if key == pygame.K_SPACE:
            self.fire_projectile(self.ship)

    def update(self):
        super().update()
        self.__check_bullet_alien_collisions()

    def __check_bullet_alien_collisions(self):
        for projectile in self.items.copy():
            if projectile.rect.bottom <= 0:
                self.items.remove(projectile)

            for alien in self.aliens:
                if projectile.rect.colliderect(alien.rect):

                    self.items.remove(projectile)
                    if alien.is_hit:
                        continue

                    alien.hit()
                    Alien.increase_speed()
                    Alien.increase_drop_speed()

                    break
