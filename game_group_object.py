import pygame


class GameGroupObject:

    def __init__(self, settings, screen):
        self.settings = settings
        self.screen = screen
        self.items = pygame.sprite.Group()

    def __len__(self):
        return len(self.items)

    def __iter__(self):
        return iter(self.items)

    def remove(self, item):
        self.items.remove(item)

    def update(self):
        self.items.update()

    def draw(self):
        self.items.draw(self.screen)
