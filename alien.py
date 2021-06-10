import pygame


class Alien(pygame.sprite.Sprite):

    fleet_direction = 1   # to the right by default
    speed_increading_factor = 1

    def __init__(self, ai_settings, screen):
        """Инициализирует инопланетный корабль и задает его начальную
        позицию."""
        super().__init__()

        self.screen = screen
        self.sc_rect = self.screen.get_rect()

        self.ai_settings = ai_settings

        self.image = pygame.transform.scale(
                pygame.image.load(ai_settings.alien_ship_img),
                (self.ai_settings.alien_ship_width,
                self.ai_settings.alien_ship_height))

        # FIX IT! : load true png with transparent background
        self.image.set_colorkey((0, 0, 0))

        self.rect = self.image.get_rect()
        self.rect.x = self.ai_settings.alien_ship_width
        self.rect.y = self.ai_settings.alien_ship_height
        self.x = float(self.rect.x)     # сохранение точной позиции
        self.y = float(self.rect.y)

    def update(self):
        self.x += Alien.fleet_direction * Alien.speed_increading_factor * \
                self.ai_settings.alien_speed_factor
        self.rect.x = self.x

    def draw(self): # или blitme?
        self.screen.blit(self.image, self.rect)

    def detect_screen_collision(self):
        return self.rect.right >= self.sc_rect.right or \
                self.rect.left <= self.sc_rect.left
