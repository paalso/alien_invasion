import pygame

class Alien():
    def __init__(self, ai_settings, screen):
        """Инициализирует инопланетный корабль и задает его начальную
        позицию."""
        super().__init__()

        self.screen = screen

        self.image = pygame.transform.scale(
                pygame.image.load("images/aliens_ship.png"),
                (ai_settings.alien_ship_width, ai_settings.alien_ship_height))
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = ai_settings.alien_ship_width
        self.rect.y = ai_settings.alien_ship_height
        self.x = float(self.rect.x)     # сохранение точной позиции


    def draw(self): # или blitme?
        self.screen.blit(self.image, self.rect)
