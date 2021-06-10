import pygame
from projectile import Projectile
from alien import Alien
from background import Background


def check_keydown_events(event, ai_settings, screen, ship, projectiles):
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_SPACE:
        projectiles.fire_projectile(ship)


def check_keyup_events(event, ship):
    if event.key == pygame.K_LEFT:
        ship.moving_left = False
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False


def check_events(ai_settings, screen, ship, projectiles):
    for event in pygame.event.get():
        if event.type == pygame.QUIT or \
                (event.type == pygame.KEYDOWN and event.key == pygame.K_q):
            return True

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, projectiles)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)


def update_screen(background, screen, ship, projectiles, aliens):

    background.draw()
    ship.update()

    projectiles.draw()
    projectiles.update(aliens)
    aliens.update()

    ship.draw()
    aliens.draw()

    pygame.display.flip()
