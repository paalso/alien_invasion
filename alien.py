import pygame, os
from game.game_object import GameObject


class Alien(GameObject, pygame.sprite.Sprite):
    hits_counter = 0
    fleet_direction = 1   # to the right by default
    speed_increase_factor = 1
    drop_speed_increase_factor = 1
    bang_sound = "assets/sounds/bang_alien.mp3"
    bang_images = "assets/images/bang_alien"
    bang_images_number = len(os.listdir(bang_images))

    def __init__(self, settings, screen):
        pygame.sprite.Sprite.__init__(self)
        GameObject.__init__(self, settings, screen)

        self.image = pygame.transform.scale(
                pygame.image.load(settings.alien_ship_img),
                (self.settings.alien_ship_width,
                self.settings.alien_ship_height))

        self.rect = self.image.get_rect()
        self.rect.x = self.settings.alien_ship_width
        self.rect.y = self.settings.alien_ship_height
        self.x = float(self.rect.x)     # сохранение точной позиции ?
        self.y = float(self.rect.y)

        self.start_speed = \
                self.settings.alien_speed * Alien.speed_increase_factor
        self.speed_increase_factor_per_alien = \
                self.settings.alien_speed_increase_factor

        self.is_hit = False
        self.is_annihilated = False

    @classmethod
    def reset_speed_increase_factors(cls,
                                    new_wave_alien_speed_increase_factor,
                                    new_wave_drop_speed_increase_factor,
                                    wave):
        Alien.speed_increase_factor = \
                new_wave_alien_speed_increase_factor ** wave
        Alien.drop_speed_increase_factor = \
                new_wave_drop_speed_increase_factor ** wave

    @classmethod
    def inverse_direction(cls):
        Alien.fleet_direction = - Alien.fleet_direction

    @classmethod
    def increase_speed(cls):
        Alien.speed_increase_factor *= Alien.annihilation_speed_increase_factor

    @classmethod
    def increase_drop_speed(cls):
        Alien.drop_speed_increase_factor *= \
                Alien.annihilation_drop_speed_increase_factor

    def hit(self):
        self.is_hit = True
        self.bang_frames_counter = 0
        pygame.mixer.Sound(Alien.bang_sound).play()

    def update(self):
        self.x += Alien.fleet_direction * Alien.speed_increase_factor * \
                self.start_speed
        self.rect.x = self.x

        if self.is_hit:
            if self.bang_frames_counter > \
                    self.settings.alien_moves_per_bang_frame * \
                    (Alien.bang_images_number - 1):
                self.is_annihilated = True
                Alien.hits_counter += 1
                return

            image_file =  "{}/{}.png".format(
                    Alien.bang_images,
                    self.bang_frames_counter // \
                    self.settings.alien_moves_per_bang_frame)

            self.image = pygame.transform.scale(
                pygame.image.load(image_file),
                (int(self.settings.alien_ship_width * \
                self.settings.alien_bang_inc_quotient),
                int(self.settings.alien_ship_height * \
                self.settings.alien_bang_inc_quotient)))
            self.bang_frames_counter += 1

    def detect_screen_collision(self):
        return self.right >= self.settings.screen_width or self.left <= 0

    def detect_get_through(self):
        return self.bottom >= self.settings.screen_height
