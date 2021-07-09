import pygame


class GameObject:

    counter = 0

    def __init__(self, settings, screen):
        GameObject.counter += 1
        self.settings = settings
        self.screen = screen
        self.sc_rect = self.screen.get_rect()
        self.speed = (0, 0)

    @property
    def left(self):
        return self.rect.left

    @property
    def right(self):
        return self.rect.right

    @property
    def top(self):
        return self.rect.top

    @property
    def bottom(self):
        return self.rect.bottom

    @property
    def width(self):
        return self.rect.width

    @property
    def height(self):
        return self.rect.height

    @property
    def center(self):
        return self.rect.center

    @property
    def centerx(self):
        return self.rect.centerx

    @property
    def centery(self):
        return self.rect.centery

    def move(self, dx, dy):
        self.rect.move_ip(dx, dy)

    def update(self):
        if self.speed == [0, 0]:
            return
        self.move(*self.speed)

    def draw(self):
        self.screen.blit(self.image, self.rect)
