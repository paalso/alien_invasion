import pygame

from game_rect_object import GameRectObject
from text_object import TextObject
from settings import Settings

empty_color = (0, 0, 0)
text_sector_start = 0.62
text_sector_len = 1 - text_sector_start


class InfoPanel(GameRectObject):   # GameObject ?
    def __init__(self, settings, screen, game):
        super().__init__(settings, screen, 0, 0,
                        settings.screen_width, settings.ship_height)
        self.game = game
        self.ship_logo = self.__generate_ship_logo()

        self.lives_left = -1
        self.score = -1
        self.shots = -1
        self.wave = -1

    def update(self):
        if self.lives_left == self.game.ship.lives_left \
                and self.wave == self.game.wave \
                and self.shots == self.game.shots \
                and self.score == self.game.score:
            return

        self.lives_left = self.game.ship.lives_left
        self.wave = self.game.wave
        self.shots = self.game.shots
        self.score = self.game.score

        self.__clear()
        self.__update_ships()
        self.__set_wave_info()
        self.__set_shots_info()
        self.__set_score_info()

    def __clear(self):
        self.surface.fill(empty_color)
        self.surface.set_colorkey(empty_color)

    # здесь все параметры изображения захардкожены, что некошерно, ну да ладно
    def __generate_ship_logo(self):
        ship_logo_scale = 0.70
        self.ship_logo_width = int(ship_logo_scale * self.settings.ship_width)
        self.ship_logo_height = int(ship_logo_scale * self.settings.ship_height)
        self.margin_top = (self.height - self.ship_logo_height) // 2
        self.ship_margin_side = self.ship_logo_width // 2

        ship_logo = pygame.transform.scale(
                    pygame.image.load(self.settings.ship_img),
                    (self.ship_logo_width, self.ship_logo_height))
        ship_logo.set_alpha(125)

        return ship_logo

    def __update_ships(self):
        x, y = self.ship_margin_side, self.margin_top
        for _ in range(self.lives_left):
            self.surface.blit(self.ship_logo, (x, y))
            x += self.ship_logo_width + self.ship_margin_side

    def __set_wave_info(self):
        self.__set_text_info(
                "Wave  {}".format(self.wave),
                text_sector_start * self.width,
                self.margin_top)

    def __set_shots_info(self):
        self.__set_text_info(
                "Shots  {}".format(self.shots),
                (text_sector_start + text_sector_len / 2) * self.width,
                self.margin_top)

    def __set_score_info(self):
        self.__set_text_info(
                "score  {}".format(self.score),
                text_sector_start * self.width,
                self.settings.info_text_size + 2 * self.margin_top, 1.2)

    def __set_text_info(self, text_content, x, y, font_inc_factor=1):
        text = TextObject(
            x, y, text_content,
            self.settings.info_text_color,
            self.settings.info_text_font,
            int(self.settings.info_text_size * font_inc_factor))
        text.draw(self.surface)
