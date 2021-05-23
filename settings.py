class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        # self.bg_color = 230, 230, 230
        self.bg_color = 15, 20, 25

        # Параметры spaceship
        self.ship_width = 50
        self.ship_height = int(self.ship_width * 1.24)
