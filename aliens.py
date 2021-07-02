import pygame

from game_group_object import GameGroupObject
from alien import Alien


class Aliens(GameGroupObject):

    def __init__(self, settings, screen, ship, game):
        super().__init__(settings, screen)
        self.counter = 0
        self.ship = ship
        self.create_fleet()
        self.number = len(self.items)
        self.fleet_drop_speed = self.settings.fleet_drop_speed
        self.bang_sound = pygame.mixer.Sound(self.settings.alien_bang_sound)
        self.game = game
        self.__set_alien_speed_increasing_parameters()

    def remove(self, alien):
        super().remove(alien)
        #self.bang_sound.play()

    def create_fleet(self):
        aliens_number_in_row = self.__get_aliens_number_in_row()
        distance_x_between_aliens = \
                self.__get_distance_x_between_aliens(aliens_number_in_row)
        number_rows = 1
        number_rows = self.__get_number_rows()

        for i in range(number_rows):
            for j in range(aliens_number_in_row):
                self.__create_alien(i, j, distance_x_between_aliens)

    def update(self):
        if len(self) == 0:
            self.__start_new_wave()

        if self.__check_aliens_screen_collision():
            self.__drop_n_change_fleet_direction()

        collided_with_ship_alien = pygame.sprite.spritecollideany(
                self.ship, self.items)

        if collided_with_ship_alien:
            self.ship.hit()
            collided_with_ship_alien.hit()

        self.__remove_annihilated_aliens()
        self.items.update()

    def __create_alien(self, row_number, alien_number, distance_between_aliens):
        alien = Alien(self.settings, self.screen)
        alien.y = (2 * row_number + 1) * self.settings.alien_ship_height
        alien.x =(alien_number + 1) * distance_between_aliens + \
                alien_number * self.settings.alien_ship_width
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.items.add(alien)

    def __get_aliens_number_in_row(self):
        screen_width = self.settings.screen_width
        alien_ship_width = self.settings.alien_ship_width
        return int(0.5 * (screen_width - alien_ship_width) / alien_ship_width)

    def __get_distance_x_between_aliens(self, aliens_number_in_row):
        screen_width = self.settings.screen_width
        alien_ship_width = self.settings.alien_ship_width
        return (screen_width - aliens_number_in_row * alien_ship_width) / \
                (aliens_number_in_row + 1)

    def __get_number_rows(self):
        screen_height = self.settings.screen_height
        ship_height = self.settings.ship_height
        alien_ship_height = self.settings.alien_ship_height
        available_y_space = screen_height - ship_height - 3 * alien_ship_height
        return available_y_space // (2 * alien_ship_height)

    def __check_aliens_screen_collision(self):
        for alien in self.items.sprites():
            if alien.detect_screen_collision():
                return True

    def __remove_annihilated_aliens(self):
        for alien in self.items.copy():
            if alien.is_annihilated:
                self.items.remove(alien)

    def __set_alien_speed_increasing_parameters(self):
        Alien.annihilation_drop_speed_increase_factor = \
                self.settings.drop_speed_increase_factor ** (1 / self.number)

        Alien.annihilation_speed_increase_factor = \
                self.settings.alien_speed_increase_factor ** (1 / self.number)

    def __drop_n_change_fleet_direction(self):

        Alien.inverse_direction()

        for alien in self.items.sprites():
            alien.y += Alien.drop_speed_increase_factor * self.fleet_drop_speed
            alien.rect.y = alien.y

    def __start_new_wave(self):
        print("Another aliens wave destoyed!!!")
        self.ship.lives_left += 1
        self.counter += 1
        Alien.reset_speed_increase_factors(
                self.settings.new_wave_alien_speed_increase_factor,
                self.settings.new_wave_drop_speed_increase_factor,
                self.counter)
        self.__clear_n_generate_wave()

    def __repeat_wave(self):
        print("Your was killed")
        self.ship.lives_left -= 1
        Alien.reset_speed_increase_factors(
                self.settings.new_wave_alien_speed_increase_factor,
                self.settings.new_wave_drop_speed_increase_factor,
                self.counter - 1)
        self.__clear_n_generate_wave()

    def __clear_n_generate_wave(self):
        self.game.projectiles.empty()
        self.ship.set_center()
        pygame.time.delay(2500)
        self.create_fleet()