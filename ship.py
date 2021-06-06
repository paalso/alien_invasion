import pygame

class Ship():
    def __init__(self, ai_settings, screen):
        """Инициализирует корабль и задает его начальную позицию."""
        self.ai_settings = ai_settings
        self.screen = screen

        self.sc_rect = self.screen.get_rect()

        self.image = pygame.transform.scale(
                pygame.image.load(ai_settings.ship_img),
                (self.ai_settings.ship_width, self.ai_settings.ship_height))

        self.rect = self.image.get_rect()

        self.rect.centerx = self.sc_rect.centerx
        self.rect.bottom = self.sc_rect.bottom
        self.centerx = float(self.rect.centerx)

        # флаги движения
        self.moving_left = False
        self.moving_right = False

    def blitme(self):
        """Рисует корабль в текущей позиции."""
        self.screen.blit(self.image, self.rect)

    def update(self):
        shift = self.ai_settings.ship_speed_factor
        if self.moving_right and self.rect.right < self.sc_rect.right:
            self.centerx += shift
        if self.moving_left and self.rect.left > self.sc_rect.left:
            self.centerx -= shift

        self.rect.centerx = self.centerx
