import sys, pygame
from settings import Settings
from game import Game
from background import Background
from ship import Ship
from aliens import Aliens
from projectiles import Projectiles


class AlienInvasion(Game):
    def __init__(self):
        super().__init__(Settings(), 'Alien Invasion')
        self.create_objects()

    def create_objects(self):
        self.create_background()
        self.create_ship()
        self.create_aliens()
        self.create_projectiles()

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
        self.projectiles = Projectiles(
                self.settings, self.screen, self.ship, self.aliens)
        self.keydown_handlers[pygame.K_SPACE].append(
                self.projectiles.handle_keydown)
        self.objects.append(self.projectiles)


def main():
    AlienInvasion().run()


if __name__ == '__main__':
    main()
