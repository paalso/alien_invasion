import pygame
import settings

class Ship():
    def __init__(self, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        ai_settings = settings.Settings()

        self.screen = screen
        self.sc_rect = self.screen.get_rect()

        self.image = pygame.transform.scale(
                pygame.image.load("images/ship.png"),
                (ai_settings.ship_width, ai_settings.ship_height))

        self.rect = self.image.get_rect()
        self.rect.centerx = self.sc_rect.centerx
        self.rect.bottom = self.sc_rect.bottom

        # флаги движения
        self.moving_left = False
        self.moving_right = False

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.rect.centerx += 1
        if self.moving_left:
            self.rect.centerx -= 1
