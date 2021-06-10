class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Параметры экрана
        self.background = "images\star_space.png"
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = 15, 20, 25

        # Параметры spaceship
        self.ship_img = "images/ship.png"
        self.ship_width = 50
        self.ship_height = int(self.ship_width * 1.24)
        self.ship_speed_factor = 1.5

        # Параметры снаряда
        self.projectile_img = "images/projectile.png"
        self.projectile_speed_factor = 0.7 * self.ship_speed_factor
        self.projectile_length = 20
        self.projectile_width = 8
        self.projectile_color = 255, 255, 0
        self.projectiles_allowed = 3

        # Параметры alien ship
        self.alien_ship_img = "images/aliens_ship.png"
        self.alien_ship_width = 75
        self.alien_ship_height = int(self.alien_ship_width * 0.75)
        self.alien_speed_factor = 0.25
        self.fleet_drop_speed = 10
        # фактор увеличения скорости к моменту, когда остается жив
        # последний alien ship
        self.drop_speed_increading_factor = 2
        self.alien_speed_increading_factor  = 2

