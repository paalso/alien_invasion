import pygame
from alien import Alien


class Aliens():
    counter = 0

    def __init__(self, ai_settings, screen):
        super().__init__()

        self.screen = screen
        self.ai_settings = ai_settings

        self.fleet = pygame.sprite.Group()
        self.create_fleet()

        self.number = len(self.fleet)
        self.fleet_drop_speed = self.ai_settings.fleet_drop_speed

        self.bang_sound = pygame.mixer.Sound(self.ai_settings.alien_bang_sound)

        print(len(self))

    def __len__(self):
        return len(self.fleet)

    def __iter__(self):
        return iter(self.fleet)

    def remove(self, alien):
        self.fleet.remove(alien)
        self.bang_sound.play()

    def update(self, ship):
        if self.__check_aliens_screen_collision():
            self.__change_fleet_direction()

        self.fleet.update()

        if pygame.sprite.spritecollideany(ship, self.fleet):
            print("Ship Hit!!!")

    def draw(self):
        self.fleet.draw(self.screen)

    def create_fleet(self):
        Aliens.counter += 1

        aliens_number_in_row = self.__get_aliens_number_in_row()
        distance_x_between_aliens = \
                self.__get_distance_x_between_aliens(aliens_number_in_row)
        number_rows = 1
        number_rows = self.__get_number_rows()

        for i in range(number_rows):
            for j in range(aliens_number_in_row):
                self.__create_alien(i, j, distance_x_between_aliens)

    def __check_aliens_screen_collision(self):
        for alien in self.fleet.sprites():
            if alien.detect_screen_collision():
                return True

    def __change_fleet_direction(self):

        # интересно, насколько некошерно так делать?
        Alien.fleet_direction = - Alien.fleet_direction
        # setattr(Alien, "fleet_direction", - Alien.fleet_direction)

        for alien in self.fleet.sprites():
            alien.y += self.fleet_drop_speed
            alien.rect.y = alien.y

    def __create_alien(self, row_number, alien_number, distance_between_aliens):
        alien = Alien(self.ai_settings, self.screen)
        alien.y = (2 * row_number + 1) * self.ai_settings.alien_ship_height
        alien.x =(alien_number + 1) * distance_between_aliens + \
                alien_number * self.ai_settings.alien_ship_width
        alien.rect.x = alien.x
        alien.rect.y = alien.y
        self.fleet.add(alien)

    def __get_aliens_number_in_row(self):
        screen_width = self.ai_settings.screen_width
        alien_ship_width = self.ai_settings.alien_ship_width
        return int(0.5 * (screen_width - alien_ship_width) / alien_ship_width)

    def __get_distance_x_between_aliens(self, aliens_number_in_row):
        screen_width = self.ai_settings.screen_width
        alien_ship_width = self.ai_settings.alien_ship_width
        return (screen_width - aliens_number_in_row * alien_ship_width) / \
                (aliens_number_in_row + 1)

    def __get_number_rows(self):
        screen_height = self.ai_settings.screen_height
        ship_height = self.ai_settings.ship_height
        alien_ship_height = self.ai_settings.alien_ship_height
        available_y_space = screen_height - ship_height - 3 * alien_ship_height
        return available_y_space // (2 * alien_ship_height)
