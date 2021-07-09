import pygame, os, pathlib
from game.game_object import GameObject


class Ship(GameObject):

    def __init__(self, settings, screen, game):

        super().__init__(settings, screen)
        self.game = game
        self.lives_left = self.settings.start_lives
        self.__load_ship_image()
        self.rect = self.image.get_rect()

        self.rect.bottom = self.sc_rect.bottom
        self.__set_center()

        self.moving_left = False
        self.moving_right = False

        self.is_hit = False
        self.is_annihilated = False

        self.bang_images_number = len(os.listdir(self.settings.bang_images))

    def reload_ship(self):
        self.__load_ship_image()
        self.is_hit = False
        self.is_annihilated = False
        self.__set_center()
        self.bang_frames_counter = 0

    def hit(self):
        self.is_hit = True
        self.bang_frames_counter = 0
        pygame.mixer.Sound(self.settings.bang_sound).play()

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
            if self.bang_frames_counter > \
                    self.settings.ship_moves_per_bang_frame * \
                    (self.bang_images_number - 1):
                self.is_annihilated = True
                self.lives_left -= 1
                return

            image_file =  pathlib.Path(self.settings.bang_images,
                    "{}.png".format(str(self.bang_frames_counter // \
                    self.settings.ship_moves_per_bang_frame)))

##            image_file =  "{}/{}.png".format(
##                    self.settings.bang_images,
##                    str(self.bang_frames_counter // \
##                    self.settings.ship_moves_per_bang_frame))


            self.image = pygame.transform.scale(
                pygame.image.load(image_file),
                (int(self.settings.ship_width * \
                    self.settings.ship_bang_inc_quotient),
                int(self.settings.ship_height * \
                    self.settings.ship_bang_inc_quotient)))
            self.image.set_colorkey((0, 0, 0))  # Fix it!

            self.bang_frames_counter += 1

    def __set_center(self):
        self.rect.centerx = self.sc_rect.centerx

    def __load_ship_image(self):
        self.image = pygame.transform.scale(
                pygame.image.load(self.settings.ship_img),
                (self.settings.ship_width, self.settings.ship_height))

    def _finish_game():
        pass
