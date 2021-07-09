import pygame
import sys
from collections import defaultdict

class Game:
    def __init__(self, settings, caption, frame_rate=60):
        self.settings = settings
        self.frame_rate = frame_rate
        self.game_over = False
        self.objects = []
        pygame.init()
        pygame.mixer.init(44100, -16, 2, 4096)
        pygame.font.init()
        self.screen = pygame.display.set_mode(
                (self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption(caption)
        self.clock = pygame.time.Clock()
        self.keydown_handlers = defaultdict(list)
        self.keyup_handlers = defaultdict(list)
        self.mouse_handlers = []
        self.quit_keys = []

    def update(self):
        for o in self.objects:
            o.update()

    def draw(self):
        for o in self.objects:
            o.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT \
            or event.type == pygame.KEYDOWN and event.key in self.quit_keys:
                self.exit_game()
            elif event.type == pygame.KEYDOWN:
                for handler in self.keydown_handlers[event.key]:
                    handler(event.key)
            elif event.type == pygame.KEYUP:
                for handler in self.keyup_handlers[event.key]:
                    handler(event.key)
            elif event.type in (pygame.MOUSEBUTTONDOWN, pygame.MOUSEBUTTONUP,
                                pygame.MOUSEMOTION):
                for handler in self.mouse_handlers:
                    handler(event.type, event.pos)

    def run(self):
        while not self.game_over:

            self.handle_events()
            self.update()
            self.draw()

            pygame.display.update()
            self.clock.tick(self.frame_rate)

    def exit_game(self):
        pygame.quit()
        sys.exit()
