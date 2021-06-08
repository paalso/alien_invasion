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


def update_screen(background, screen, ship, projectiles, aliens):

    background.blitme()

    ship.update()

    for projectile in projectiles.sprites():
        projectile.update()
        projectile.draw()

    update_projectiles(projectiles)
    update_aliens(aliens)
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

    aliens_number_in_row = get_aliens_number_in_row(ai_settings)

    distance_x_between_aliens = get_distance_x_between_aliens(
            aliens_number_in_row, ai_settings)

    number_rows = get_number_rows(ai_settings)

    for i in range(number_rows):
        for j in range(aliens_number_in_row):
            create_alien(
                    ai_settings, screen, aliens,
                    i, j, distance_x_between_aliens)


def get_aliens_number_in_row(ai_settings):
    return int(0.5 * (
            ai_settings.screen_width - ai_settings.alien_ship_width) \
            / ai_settings.alien_ship_width)


def get_distance_x_between_aliens(aliens_number_in_row, ai_settings):
    return (ai_settings.screen_width - \
            aliens_number_in_row * ai_settings.alien_ship_width) / \
            (aliens_number_in_row + 1)


def get_number_rows(ai_settings):
    available_y_space = ai_settings.screen_height - ai_settings.ship_height - \
                        3 * ai_settings.alien_ship_height
    return available_y_space // (2 * ai_settings.alien_ship_height)


def create_alien(
            ai_settings, screen, aliens,
            row_number, alien_number, distance_between_aliens):

    alien = Alien(ai_settings, screen)
    alien.y = (2 * row_number + 1) * ai_settings.alien_ship_height
    alien.x =(alien_number + 1) * distance_between_aliens + \
            alien_number * ai_settings.alien_ship_width
    alien.rect.x = alien.x
    alien.rect.y = alien.y
    aliens.add(alien)


def update_aliens(aliens):
    if check_aliens_screen_collision(aliens):
        change_fleet_direction()
    else:
        restore_fleet()

    aliens.update()


def check_aliens_screen_collision(aliens):
    for alien in aliens.sprites():
        if alien.detect_screen_collision():
            return True
    return False


def change_fleet_direction():
    setattr(Alien, "fleet_direction", - Alien.fleet_direction)
    setattr(Alien, "fleet_drop", True)


def restore_fleet():
    setattr(Alien, "fleet_drop", False)
