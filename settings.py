import colors


class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        # Screen parameters
        self.background = "images/star_space.png"
        self.screen_width = 700
        self.screen_height = 500
        self.bg_color = 15, 20, 25

        # Spaceship parameters
        self.ship_img = "images/ship.png"
        self.ship_width = 50
        self.ship_height = int(self.ship_width * 1.24)
        self.ship_speed = 8

        # Projectile parameters
        self.projectile_img = "images/projectile.png"
        self.projectile_launch_sound = "sounds/launch.mp3"
        self.projectile_speed = 0.7 * self.ship_speed
        self.projectile_length = 15
        self.projectile_width = 5
        self.projectile_color = 255, 255, 0
        self.projectiles_allowed = 3

        # Alien Ship parameters
        self.alien_ship_img = "images/aliens_ship.png"
        self.alien_bang_sound = "sounds/bang.mp3"
        self.moves_per_bang_frame = 3
        self.alien_ship_width = 75
        self.alien_ship_height = int(self.alien_ship_width * 0.75)
        self.alien_speed = 0.20 * self.ship_speed
        self.fleet_drop_speed = 10
        # факторы увеличения скоростей (горизонтальной и вериткальной)
        # смещения к моменту, когда остается жив последний alien ship
        self.drop_speed_increase_factor = 2
        self.alien_speed_increase_factor  = 2
        # факторы увеличения начальных скоростей
        # (горизонтальной и вериткальной) следующей волны
        self.new_wave_drop_speed_increase_factor = 1.20
        self.new_wave_alien_speed_increase_factor  = 1.20

        self.button_position = \
                self.screen_width // 2, self.screen_height // 2, 150, 40
        self.button_text_color = colors.WHITE
        self.button_text_font = None
        self.button_text_size = 30
        self.button_normal_back_color = colors.GREEN
        self.button_hover_back_color = colors.GREEN3
        self.button_pressed_back_color = colors.GREEN2