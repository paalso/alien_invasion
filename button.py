import pygame

from game_rect_object import GameRectObject
from text_object import TextObject
# from settings import Settings


class Button(GameRectObject):   # GameObject ?
    def __init__(self, settings, screen, x, y, w, h, text,
                on_click=lambda x: None, press_key=None,
                padding=0, centralized=False, text_centralize=False):
        super().__init__(settings, screen, x, y, w, h)
        self.text_centralize = text_centralize
        self.text_content = text

        # if centralized center = x, y else topleft = x, y
        if centralized:
            self.rect.center = (self.left, self.top)
        else:
            self.rect.topleft = (self.left, self.top)

        self.state = 'normal'
        self.on_click = on_click
        self.press_key = press_key

        # text in the center of the button if text_centralize
        text_x, text_y = \
                (self.width // 2, self.height // 2) if text_centralize \
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
        super().draw()

    def handle_keyup(self, key):
        if self.press_key and key == self.press_key:
            self.state = 'pressed'
            self.on_click()
        self.state = 'normal'

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
            self.on_click()
            self.state = 'hover'
