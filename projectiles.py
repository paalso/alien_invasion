import pygame
from ship import Ship
from projectile import Projectile
from alien import Alien


class Projectiles():

    def __init__(self, ai_settings, screen, aliens):
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        self.projectiles = pygame.sprite.Group()

        self.drop_speed_increasing_factor_per_alien = \
                self.ai_settings.drop_speed_increading_factor ** \
                (1 / aliens.number)

        self.speed_increasing_factor_per_alien = \
                self.ai_settings.alien_speed_increading_factor ** \
                (1 / aliens.number)

    def __iter__(self):
        return iter(self.projectiles)

    def update(self, aliens):
        self.projectiles.update()
        for projectile in self.projectiles.copy():
            if projectile.rect.bottom <= 0:
                self.projectiles.remove(projectile)

            for alien in aliens:
                if projectile.rect.colliderect(alien.rect):
                    self.projectiles.remove(projectile)
                    aliens.remove(alien)
                    aliens.fleet_drop_speed *= \
                            self.drop_speed_increasing_factor_per_alien
                    setattr(Alien, "speed_increading_factor",
                            Alien.speed_increading_factor * \
                            self.speed_increasing_factor_per_alien)
                    break

    def draw(self):
        self.projectiles.draw(self.screen)

    def fire_projectile(self, ship):
        if len(self.projectiles) < self.ai_settings.projectiles_allowed:
            projectile = Projectile(self.ai_settings, self.screen, ship)
            self.projectiles.add(projectile)


