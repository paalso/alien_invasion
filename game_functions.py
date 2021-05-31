import pygame
from projectile import Projectile


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
        if event.type == pygame.QUIT:
            return True

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, projectiles)

        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

    return False


def update_screen(ai_settings, screen, ship, projectiles):
    screen.fill(ai_settings.bg_color)
    ship.update()
    for projectile in projectiles.sprites():
        projectile.update()
        projectile.draw()
    update_projectiles(projectiles)
    ship.blitme()
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
