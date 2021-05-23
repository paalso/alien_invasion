import pygame


def check_events(ship):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                ship.moving_left = True
            if event.key == pygame.K_RIGHT:
                ship.moving_right = True

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                ship.moving_left = False
            if event.key == pygame.K_RIGHT:
                ship.moving_right = False

    return False


def update_screen(screen, ship, bg_color):
    screen.fill(bg_color)
    ship.update()
    ship.blitme()
    pygame.display.flip()
