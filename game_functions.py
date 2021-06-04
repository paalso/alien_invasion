import pygame
from projectile import Projectile
from alien import Alien


def check_keydown_events(event, ai_settings, screen, ship, projectiles):
    if event.key == pygame.K_LEFT:
        ship.moving_left = True
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    if event.key == pygame.K_SPACE:
        fire_projectile(ai_settings, screen, ship, projectiles)


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


def update_screen(ai_settings, screen, ship, projectiles, aliens):
    screen.fill(ai_settings.bg_color)
    ship.update()
    for projectile in projectiles.sprites():
        projectile.update()
        projectile.draw()
    update_projectiles(projectiles)
    ship.blitme()
    aliens.draw(screen)
    pygame.display.flip()


def update_projectiles(projectiles):
    for projectile in projectiles.copy():
        if projectile.rect.bottom <= 0:
            projectiles.remove(projectile)
            del projectile


def fire_projectile(ai_settings, screen, ship, projectiles):
    if len(projectiles) < ai_settings.bullets_allowed:
        projectile = Projectile(ai_settings, screen, ship)
        projectiles.add(projectile)


def create_fleet(ai_settings, screen, aliens):

    aliens_number_in_row = get_aliens_number_in_row(
            ai_settings.screen_width, ai_settings.alien_ship_width)

    distance_between_aliens = get_distance_between_aliens(
            aliens_number_in_row,
            ai_settings.screen_width, ai_settings.alien_ship_width)

    for i in range(aliens_number_in_row):
        create_alien(
                ai_settings, screen, aliens, i, distance_between_aliens)


def get_aliens_number_in_row(screen_width, alien_ship_width):
    return int(0.5 * (screen_width - alien_ship_width) / alien_ship_width)


def get_distance_between_aliens(aliens_number_in_row,
                                screen_width, alien_ship_width):
    return (screen_width - aliens_number_in_row * alien_ship_width) / \
            (aliens_number_in_row + 1)


def create_alien(
        ai_settings, screen, aliens, alien_number, distance_between_aliens):

    alien = Alien(ai_settings, screen)
    alien.x =(alien_number + 1) * distance_between_aliens + \
            alien_number * ai_settings.alien_ship_width
    alien.rect.x = alien.x
    aliens.add(alien)
