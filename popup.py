import pygame
import pygame.freetype
from game_rect_object import GameRectObject

EMPTY_COLOR = (0, 0, 0)


def word_wrap(surf, text, font, color=EMPTY_COLOR):
    font.origin = True
    words = text.split(' ')
    width, height = surf.get_size()
    line_spacing = font.get_sized_height() + 2
    x, y = 0, line_spacing
    space = font.get_rect(' ')
    for word in words:
        bounds = font.get_rect(word)
        if x + bounds.width + bounds.x >= width:
            x, y = 0, y + line_spacing
        if x + bounds.width + bounds.x >= width:
            raise ValueError("word too wide for the surface")
        if y + bounds.height - bounds.y >= height:
            raise ValueError("text to long for the surface")
        font.render_to(surf, (x, y), None, color)
        x += bounds.width + space.width
    return x, y


class Popup(GameRectObject):   # GameObject ?

    def __init__(self, settings, screen, x, y, w, h, text,
                color, back_color, font_name, font_size, transparent=False,
                on_click=lambda x: None, press_key=None, centralized=False):
        super().__init__(settings, screen, x, y, w, h)

        self.back_color = back_color if back_color else EMPTY_COLOR

        self.transparent = transparent
        self.state = 'normal'
        self.on_click = on_click
        self.press_key = press_key

        self.text = text
        self.color = color
        self.font = pygame.freetype.SysFont(font_name, font_size)

        # if centralized center = x, y else topleft = x, y
        if centralized:
            self.rect.center = (self.left, self.top)
        else:
            self.rect.topleft = (self.left, self.top)

    def draw(self):
        if self.transparent:
            self.surface.fill(EMPTY_COLOR)
            self.surface.set_colorkey(EMPTY_COLOR)
        else:
            self.surface.fill(self.back_color)

        word_wrap(self.surface, self.text, self.font, self.color)
        super().draw()

    def handle_keyup(self, key):
        if self.press_key and key == self.press_key:
            self.state = 'pressed'
            self.on_click(self)
        self.state = 'normal'

    def set_text(self, text_content):
        pass

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
