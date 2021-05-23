import sys, pygame
from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():

    pygame.init()

    ai_settings = Settings()

    screen_size = ai_settings.screen_width, ai_settings.screen_height
    bg_color = ai_settings.bg_color
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Alien Invasion")
    screen.fill(bg_color)

    ship = Ship(screen)

    # Рисование
    finished = False

    # Можно еще упростить
    # while not gf.check_events():

    while not finished:
        finished = gf.check_events(ship)
        gf.update_screen(screen, ship, bg_color)

    print("Good bye!")
    pygame.quit()


run_game()
