import pygame

from game_object import GameObject
from text_object import TextObject
# from settings import Settings


class Button(GameObject):   # GameObject ?
    def __init__(self, settings, screen, x, y, w, h, text,
                on_click=lambda x: None, padding=0,
                centralized=False, text_centralize=False):
        self.settings = settings
        self.screen = screen
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.speed = (0, 0)
        self.text_centralize = text_centralize
        self.text_content = text

        self.surface = pygame.Surface((self.w, self.h))
        self.rect = self.surface.get_rect()
        if centralized:
            self.rect.center = (self.x, self.y)
        else:
            self.rect.topleft = (self.x, self.y)

        self.state = 'normal'
        self.on_click = on_click

        # text in the center of the button if text_centralize
        text_x, text_y = (self.w // 2, self.h // 2) if text_centralize \
                        else (padding, padding)
        self.text = TextObject(
                text_x, text_y, text,
                self.settings.button_text_color,
                self.settings.button_text_font,
                self.settings.button_text_size)

        self.back_colors = \
                dict(
                    normal=self.settings.button_normal_back_color,
                    hover=self.settings.button_hover_back_color,
                    pressed=self.settings.button_pressed_back_color
                )

    @property
    def back_color(self):
        return self.back_colors[self.state]

    def set_text(self, text_content):
        pass

    def draw(self):
        self.surface.fill(self.back_color)
        self.text.draw(self.surface, self.text_centralize)
        self.screen.blit(self.surface, self.rect)

    def handle_mouse_event(self, type, pos):
        if type == pygame.MOUSEMOTION:
            self.handle_mouse_move(pos)
        elif type == pygame.MOUSEBUTTONDOWN:
            self.handle_mouse_down(pos)
        elif type == pygame.MOUSEBUTTONUP:
            self.handle_mouse_up(pos)

    def handle_mouse_move(self, pos):
        if self.rect.collidepoint(pos):
            if self.state != 'pressed':
                self.state = 'hover'
        else:
            self.state = 'normal'

    def handle_mouse_down(self, pos):
        if self.rect.collidepoint(pos):
            self.state = 'pressed'

    def handle_mouse_up(self, pos):
        if self.state == 'pressed':
            self.on_click(self)
            self.state = 'hover'
