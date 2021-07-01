import sys, pygame
import colors
from settings import Settings
from game import Game
from button import Button
from background import Background
from ship import Ship
from aliens import Aliens
from projectiles import Projectiles


class AlienInvasion(Game):
    def __init__(self):
        super().__init__(Settings(), 'Alien Invasion')
        self.quit_keys = [pygame.K_q]
        self.menu_buttons = []  # ?
        self.create_objects()

        self.is_game_running = True
        self.state = "start"    # "game", "pause", "finish"
        self.keydown_handlers[pygame.K_c].append(self.handle_keydown)
        self.keydown_handlers[pygame.K_p].append(self.handle_keydown)
        self.keyup_handlers[pygame.K_s].append(self.handle_keyup)

    def handle_keyup(self, key):
        if self.state == "start" and key == pygame.K_s:
            self.__start_game()

    def handle_keydown(self, key):
        if self.state == "game" and key == pygame.K_p:
            self.state = "pause"
            self.__create_on_play_button("CONTINUE")

        elif self.state == "pause" and key in (pygame.K_c, pygame.K_p):
            self.state = "game"
            self.__remove_menu()

    def create_objects(self):
        self.create_background()
        self.create_menu()
        self.create_ship()
        self.create_aliens()
        self.create_projectiles()

    def create_menu(self):  # ?!
        self.__create_on_play_button("START")

    def create_background(self):
        self.background = Background(self.settings, self.screen)
        self.objects.append(self.background)

    def create_ship(self):
        ship = Ship(self.settings, self.screen)
        self.keydown_handlers[pygame.K_LEFT].append(ship.handle_keydown)
        self.keydown_handlers[pygame.K_RIGHT].append(ship.handle_keydown)
        self.keyup_handlers[pygame.K_LEFT].append(ship.handle_keyup)
        self.keyup_handlers[pygame.K_RIGHT].append(ship.handle_keyup)
        self.ship = ship
        self.objects.append(self.ship)

    def create_aliens(self):
        self.aliens = Aliens(self.settings, self.screen, self.ship)
        self.objects.append(self.aliens)

    def create_projectiles(self):
        self.projectiles = Projectiles(             # , self !
                self.settings, self.screen, self.ship, self.aliens, self)
        self.keydown_handlers[pygame.K_SPACE].append(
                self.projectiles.handle_keydown)
        self.objects.append(self.projectiles)

    def update(self):
        if self.state != "game":
            return

        super().update()

    def draw(self):
        if self.state == "start":
            self.background.draw()
            self.__draw_menu()
            return

        super().draw()

    def __create_on_play_button(self, text):

        def on_play(button):
            self.__start_game()

        on_play_button = Button(self.settings, self.screen,
                *self.settings.button_position, text,
                on_click=on_play, centralized=True, text_centralize=True)

        self.menu_buttons.append(on_play_button)
        self.objects.append(on_play_button)
        self.mouse_handlers.append(on_play_button.handle_mouse_event )

        return on_play_button

    def __draw_menu(self):
        for b in self.menu_buttons:
            b.draw()

    def __remove_menu(self):
        for b in self.menu_buttons:
            self.objects.remove(b)
        self.menu_buttons.clear()

    def __start_game(self):
        self.__remove_menu()
        self.is_game_running = True
        self.state = "game"
