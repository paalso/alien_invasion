import pygame, os
from game_object import GameObject


class Alien(GameObject, pygame.sprite.Sprite):

    fleet_direction = 1   # to the right by default
    speed_increase_factor = 1
    bang_sound = "sounds/bang.mp3"
    bang_images = "images/bang"
    bang_images_number = len(os.listdir(bang_images))

    def __init__(self, settings, screen):
        pygame.sprite.Sprite.__init__(self)
        GameObject.__init__(self, settings, screen)

        self.sc_rect = self.screen.get_rect()

        self.image = pygame.transform.scale(
                pygame.image.load(settings.alien_ship_img),
                (self.settings.alien_ship_width,
                self.settings.alien_ship_height))

        self.rect = self.image.get_rect()
        self.rect.x = self.settings.alien_ship_width
        self.rect.y = self.settings.alien_ship_height
        self.x = float(self.rect.x)     # сохранение точной позиции
        self.y = float(self.rect.y)

        self.is_hit = False
        self.is_annihilated = False

    def hit(self):
        self.is_hit = True
        self.hit_counter = 0
        pygame.mixer.Sound(Alien.bang_sound).play()

    def update(self):
        self.x += Alien.fleet_direction * Alien.speed_increase_factor * \
                self.settings.alien_speed
        self.rect.x = self.x

        if self.is_hit:
            if self.hit_counter > self.settings.moves_per_bang_frame * \
                                    (Alien.bang_images_number - 1):
                self.is_annihilated = True
                del(self)
                return

            image_file =  "{}/{}.png".format(
                    Alien.bang_images,
                    self.hit_counter // self.settings.moves_per_bang_frame)
            self.image = pygame.transform.scale(
                pygame.image.load(image_file),
                (int(self.settings.alien_ship_width * 1.5),
                int(self.settings.alien_ship_height * 1.5)))
            self.hit_counter += 1

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def detect_screen_collision(self):
        return self.rect.right >= self.sc_rect.right or \
                self.rect.left <= self.sc_rect.left
