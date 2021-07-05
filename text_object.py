import pygame


class TextObject:
    def __init__(self, x, y, text, color, font_name, font_size):
        self.pos = x, y
        self.text = text
        self.color = color
        # self.font = pygame.font.SysFont(font_name, font_size)
        self.font = pygame.font.Font(font_name, font_size)
        self.surface, self.rect = self.get_surface(text)
        self.rect.topleft = self.pos

    def draw(self, surface, centralized=False):
        if centralized:
            x, y = self.rect.topleft
            x = x - self.rect.width / 2
            y = y - self.rect.height / 2
            surface.blit(self.surface, (x, y))
        else:
            surface.blit(self.surface, self.rect)

    def get_surface(self, text):
        text_surface = self.font.render(text, True, self.color)
        return text_surface, text_surface.get_rect()

    def update(self):
        pass
