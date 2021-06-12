import sys, pygame
from settings import Settings
from background import Background
from ship import Ship
from aliens import Aliens
from projectiles import Projectiles
import game_functions as gf


def run_game():

    pygame.init()
    ai_settings = Settings()
    screen_size = ai_settings.screen_width, ai_settings.screen_height
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Alien Invasion")

    # создание корабля, группы пуль и пришельцев
    background = Background(ai_settings, screen)
    aliens = Aliens(ai_settings, screen)
    projectiles = Projectiles(ai_settings, screen, aliens)
    ship = Ship(ai_settings, screen)

    # Рисование
    finished = False

    # Можно еще упростить ?
    # while not gf.check_events():

    while not finished:
        finished = gf.check_events(ai_settings, screen, ship, projectiles)
        gf.update_screen(background, screen, ship, projectiles, aliens)

    print("Good bye!")
    pygame.quit()


run_game()
