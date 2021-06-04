import sys, pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    pygame.init()

    ai_settings = Settings()

    screen_size = ai_settings.screen_width, ai_settings.screen_height

    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Alien Invasion")
    screen.fill(ai_settings.bg_color)

    # создание корабля, группы пуль и пришельцев
    ship = Ship(ai_settings, screen)
    projectiles = pygame.sprite.Group()
    aliens = pygame.sprite.Group()
    gf.create_fleet(ai_settings, screen, aliens)

    # Рисование
    finished = False

    # Можно еще упростить ?
    # while not gf.check_events():

    while not finished:
        finished = gf.check_events(ai_settings, screen, ship, projectiles)
        gf.update_screen(ai_settings, screen, ship, projectiles, aliens)

    print("Good bye!")
    pygame.quit()


run_game()
