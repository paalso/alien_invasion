import sys, pygame


def run_game():

    pygame.init()

    screen_size = 1200, 800
    bg_color = 230, 230, 230
    screen = pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Alien Invasion")
    screen.fill(bg_color)

    # Рисование
    finished = False

    while not finished:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finished = True

        screen.fill(bg_color)
        pygame.display.flip()

    print("Good bye!")
    pygame.quit()


run_game()
