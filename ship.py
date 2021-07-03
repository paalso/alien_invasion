import pygame, os
from game_object import GameObject


class Ship(GameObject):

    bang_sound = "sounds/bang_ship.mp3"
    bang_images = "images/bang_ship"
    bang_images_number = len(os.listdir(bang_images))

    def __init__(self, settings, screen, game):

        super().__init__(settings, screen)
        self.game = game
        self.lives_left = self.settings.lives
        self.image = pygame.transform.scale(
                pygame.image.load(settings.ship_img),
                (self.settings.ship_width, self.settings.ship_height))
        self.rect = self.image.get_rect()

        self.rect.bottom = self.sc_rect.bottom
        self.set_center()

        self.moving_left = False
        self.moving_right = False

        self.is_hit = False
        self.is_annihilated = False

    def hit(self):
        self.is_hit = True
        self.hit_counter = 0
        pygame.mixer.Sound(Ship.bang_sound).play()

    def handle_keydown(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = True
        if key == pygame.K_RIGHT:
            self.moving_right = True

    def handle_keyup(self, key):
        if key == pygame.K_LEFT:
            self.moving_left = False
        if key == pygame.K_RIGHT:
            self.moving_right = False

    def update(self):
        shift = self.settings.ship_speed
        if self.moving_right and self.right < self.sc_rect.right:
            self.move(shift, 0)
        if self.moving_left and self.left > self.sc_rect.left:
            self.move(-shift, 0)

        # Этот фрагмент практически повторяет аналогичный из класса Alien
        # и с этим надо бы что-то делать
        if self.is_hit:
            if self.hit_counter > self.settings.ship_moves_per_bang_frame * \
                                    (Ship.bang_images_number - 1):
                self.is_annihilated = True
                return

            image_file =  "{}/{}.png".format(
                    Ship.bang_images,
                    str(self.hit_counter // self.settings.ship_moves_per_bang_frame))

            self.image = pygame.transform.scale(
                pygame.image.load(image_file),
                (int(self.settings.ship_width * self.settings.ship_bang_inc_quotient),
                int(self.settings.ship_height * self.settings.ship_bang_inc_quotient)))
            self.image.set_colorkey((0, 0, 0))  # Fix it!

            self.hit_counter += 1

        if self.is_annihilated:
            self.game.state = "finish"

    def set_center(self):
        self.rect.centerx = self.sc_rect.centerx

    def _finish_game():
        pass
