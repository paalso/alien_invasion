class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""
    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = 15, 20, 25

        # Параметры spaceship
        self.ship_width = 50
        self.ship_height = int(self.ship_width * 1.24)
        self.ship_speed_factor = 1.0

        # Параметры снаряда
        self.projectile_speed_factor = 0.7 * self.ship_speed_factor
        self.projectile_length = 10
        self.projectile_width = 3
        self.projectile_color = 255, 255, 0
        self.bullets_allowed =  3

        # Параметры alien ship
        self.alien_ship_width = 50
        self.alien_ship_height = int(self.alien_ship_width * 0.75)
