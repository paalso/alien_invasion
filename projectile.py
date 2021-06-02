import pygame

class Projectile(pygame.sprite.Sprite):
    def __init__(self, ai_settings, screen, ship):
        super().__init__()

        self.screen = screen
        self.ship = ship
        self.speed_factor = ai_settings.projectile_speed_factor
        self.color = ai_settings.projectile_color

        # сначала создаем снаряд в позиции (0, 0)
        self.rect = pygame.Rect((0, 0,
                ai_settings.projectile_width, ai_settings.projectile_length))

        # назначаем правильную позицию, связанную с кораблем
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top

        # позиция снаряда хранится в вещественном формате - почему и зачем?
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.speed_factor
        self.rect.y = self.y

    def draw(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
