import pygame
from ship import Ship
from projectile import Projectile


class Projectiles():

    def __init__(self, ai_settings, screen):
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        self.projectiles = pygame.sprite.Group()

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
                    break

    def draw(self):
        self.projectiles.draw(self.screen)

    def fire_projectile(self, ship):
        if len(self.projectiles) < self.ai_settings.projectiles_allowed:
            projectile = Projectile(self.ai_settings, self.screen, ship)
            self.projectiles.add(projectile)


