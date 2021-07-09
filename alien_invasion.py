import os, random, time
import pygame
import colors
from settings import Settings
from game import Game
from background import Background
from info_panel import InfoPanel
from button import Button
from ship import Ship
from alien import Alien
from aliens import Aliens
from projectiles import Projectiles

from popup import Popup


def empty_func():
    pass


class AlienInvasion(Game):
    def __init__(self):
        super().__init__(Settings(), 'Alien Invasion')
        self.quit_keys = [pygame.K_q]
        self.menu_buttons = []  # ?
        self.popups = []  # ?
        self.create_objects()

        self.state = "start" # "game", "pause", "new wave", "endgame", "slides"
        self.keydown_handlers[pygame.K_p].append(self.handle_keydown)

        self.start_ticks = 0
        self.pause_finished = False

    @property
    def lives_left(self):
        return self.ship.lives_left

    @property
    def score(self):
        return Alien.hits_counter

    @property
    def shots(self):
        return self.projectiles.shots

    @property
    def wave(self):
        return self.aliens.counter

    def handle_keyup(self, key):    # ???
        pass

    def handle_keydown(self, key):
        if self.state == "game" and key == pygame.K_p:
            self.state = "pause"
            self.__create_on_play_button("CONTINUE", pygame.K_c)

    def create_objects(self):
        self.create_background()
        self.create_menu()
        self.create_ship()
        self.create_aliens()
        self.create_projectiles()
        self.create_info_panel()

    def create_background(self):
        self.background = Background(self.settings, self.screen)
        self.objects.append(self.background)

    def create_menu(self):  # ?!
        self.__create_on_play_button("START", pygame.K_s)

    def create_info_panel(self):
        self.info_panel = InfoPanel(self.settings, self.screen, self)
        self.objects.append(self.info_panel)

    def create_ship(self):
        ship = Ship(self.settings, self.screen, self)
        self.keydown_handlers[pygame.K_LEFT].append(ship.handle_keydown)
        self.keydown_handlers[pygame.K_RIGHT].append(ship.handle_keydown)
        self.keyup_handlers[pygame.K_LEFT].append(ship.handle_keyup)
        self.keyup_handlers[pygame.K_RIGHT].append(ship.handle_keyup)
        self.ship = ship
        self.objects.append(self.ship)

    def create_aliens(self):
        self.aliens = Aliens(self.settings, self.screen, self.ship, self)
        self.objects.append(self.aliens)

    def create_projectiles(self):
        self.projectiles = Projectiles(
                self.settings, self.screen, self.ship, self.aliens, self)
        self.keydown_handlers[pygame.K_SPACE].append(
                self.projectiles.handle_keydown)
        self.objects.append(self.projectiles)

    def update(self):
        if self.state == "endgame":
            self.__endgame()

        if self.state == "new wave":
            self.__start_new_wave()

        if self.state == "slides":
            self.background.set_image(self.slides[self.slides_counter])
            self.slides_counter += 1
            pygame.time.delay(int(self.settings.slide_delay * 1000))
            if self.slides_counter == len(self.slides):
                self.exit_game()

        if self.state != "game":
            return

        super().update()

    def draw(self):
        if self.state == "start":
            self.background.draw()
            self.__draw_menu()
            return

        super().draw()

    def __draw_menu(self):
        for b in self.menu_buttons:
            b.draw()

    def __remove_menu(self):
        self.__remove_some_objects(self.menu_buttons)

    def __remove_popups(self):
        self.__remove_some_objects(self.popups)

    def __remove_some_objects(self, some_objects):
        for o in some_objects:
            self.objects.remove(o)
            if "press_key" in o.__dict__:
                key = o.press_key
                self.keyup_handlers[key].remove(o.handle_keyup)
                self.mouse_handlers.remove(o.handle_mouse_event )

        some_objects.clear()

    def __create_on_play_button(self, text, key=None):

        def on_play():
            self.__remove_menu()
            self.state = "game"

        on_play_button = Button(self.settings, self.screen,
                *self.settings.button_position, text, on_click=on_play,
                press_key=key, centralized=True, text_centralize=True)

        self.menu_buttons.append(on_play_button)
        self.objects.append(on_play_button)
        self.mouse_handlers.append(on_play_button.handle_mouse_event )

        if key:
            self.keyup_handlers[key].append(on_play_button.handle_keyup)

    def __start_new_wave(self):

        def action():
            self.state = "game"
            self.aliens.start_new_wave()

        self.__delay(self.settings.msg_new_wave_delay,
                    self.__create_new_wave_message, action,)

    def __endgame(self):

        def action():
            self.state = "slides"
            self.__clear_background()
            self.slides_counter = 0
            self.slides = ["{}{}".format(self.settings.slides_directory, slide)
                    for slide in os.listdir(self.settings.slides_directory)]
            random.shuffle(self.slides)

        self.__delay(self.settings.msg_new_wave_delay,
                    self.__create_endgame_message, action)

    def __create_endgame_message(self):

        text = self.settings.msg_endgame_text
        self.__create_message(text, 240, 120, 470, 300)

    def __create_new_wave_message(self):

        text = self.settings.msg_new_wave_text

        if self.wave == 1:
            text = text.replace("yet another", "   the first")
        elif self.wave == 2:
            text = text.replace("yet another", "   the second")

        self.__create_message(text, 200, 100, 400, 300)

    def __create_message(self, text, left_shift, up_shift, width, height):

        def on_play():
            self.__remove_popups()
            self.pause_finished = True

        position = (self.settings.screen_width // 2 - left_shift,
                    self.settings.screen_height // 2 - up_shift,
                    width, height)

        popup = Popup(self.settings, self.screen, *position,
                text, colors.RED1, None, font_name=self.settings.msg_text_font,
                font_size=self.settings.msg_text_size,
                on_click=on_play, press_key=pygame.K_c,
                transparent=True, centralized=False)

        self.popups.append(popup)
        self.objects.append(popup)

        self.mouse_handlers.append(popup.handle_mouse_event )
        self.keyup_handlers[pygame.K_c].append(popup.handle_keyup)

    def __delay(self, duration, message=empty_func, action=empty_func):        # ?
        if not self.start_ticks:
            self.start_ticks = pygame.time.get_ticks()
            message()

        elif self.pause_finished or self.start_ticks >= 0 and \
                pygame.time.get_ticks() - self.start_ticks > \
                duration * 1000:
            self.pause_finished = False
            self.start_ticks = 0
            self.__remove_popups()
            action()

    def __clear_background(self, save_object_instance=Background):
        for o in self.objects.copy():
            if not isinstance(o, save_object_instance):
                self.objects.remove(o)
