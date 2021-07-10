import game.colors as colors
from pathlib import Path


class Settings():
    """Класс для хранения всех настроек игры Alien Invasion."""

    def __init__(self):
        """Инициализирует настройки игры."""
        assets_path = Path(Path.cwd(), "assets")
        images_path = Path(assets_path, "images")
        sounds_path = Path(assets_path, "sounds")
        fonts_path = Path(assets_path, "fonts")

        # Screen parameters
        self.background = Path(images_path, "star_space.jpg")
        self.screen_width = 960
        self.screen_height = 720
        self.bg_color = 15, 20, 25

        # Spaceship parameters
        self.ship_img = Path(images_path, "ship.png")
        self.start_lives = 1
        self.ship_width = 50
        self.ship_height = int(self.ship_width * 1.24)
        self.ship_speed = 8
        self.ship_moves_per_bang_frame = 1
        self.ship_bang_inc_quotient = 2
        self.bang_sound = Path(sounds_path, "bang_ship.mp3")
        self.bang_images = Path(images_path, "bang_ship")

        # Projectile parameters
        self.projectile_img = Path(images_path, "projectile.png")
        self.projectile_launch_sound = Path(sounds_path, "launch.mp3")
        self.projectile_speed = 0.7 * self.ship_speed
        self.projectile_length = 15
        self.projectile_width = 5
        self.projectile_color = 255, 255, 0
        self.projectiles_allowed = 3

        # Alien Ship parameters
        self.alien_ship_img = Path(images_path, "aliens_ship.png")
        self.alien_bang_sound = Path(sounds_path, "bang_alien.mp3")
        self.alien_ship_width = 75
        self.alien_ship_height = int(self.alien_ship_width * 0.75)
        self.alien_speed = 0.20 * self.ship_speed
        self.fleet_drop_speed = 10
        self.alien_moves_per_bang_frame = 3
        self.alien_bang_inc_quotient = 1.5

        # факторы увеличения скоростей (горизонтальной и вериткальной)
        # смещения к моменту, когда остается жив последний alien ship
        # т.е. в пределах уровня скорости возрастают, но к началу
        # следующего - падают, но до значения выше, чем пройденном
        self.drop_speed_increase_factor = 2
        self.alien_speed_increase_factor  = 2

        # факторы увеличения начальных скоростей
        # (горизонтальной и вериткальной) следующей волны
        self.new_wave_drop_speed_increase_factor = 1.15
        self.new_wave_alien_speed_increase_factor  = 1.15

        self.button_position = \
                self.screen_width // 2, self.screen_height // 2, 150, 40
        self.button_text_color = colors.WHITE
        self.button_text_font = Path(fonts_path, "Alenia.ttf")
        self.button_text_font = Path(fonts_path, "panicbuttonbb_reg.ttf")
        self.button_text_size = 30
        self.button_normal_back_color = colors.GREEN
        self.button_hover_back_color = colors.GREEN3
        self.button_pressed_back_color = colors.GREEN2

        self.info_text_color = colors.RED3
        self.info_text_font = Path(fonts_path, "Alien.ttf")
        self.info_text_size = int(0.3 * self.ship_height)

        self.msg_new_wave_delay = 4
        self.msg_text_color = colors.RED2
        self.msg_text_font = Path(fonts_path, "Alien.ttf")
        self.msg_text_font = None
        self.msg_text_size = int(0.6 * self.ship_height)
        self.msg_new_wave_text = \
            "You have repelled yet another Alien Wave. " + \
            "But the next one, even more dangerous and ruthless, is coming..."

        self.msg_endgame_delay = 5   # 5
        self.msg_endgame_text = \
            "You fought bravely        " + \
            "But the enemy defeated us " + \
            "Now the Earth is under the rule of the evil aliens        " + \
            "For ever and ever..."

        self.help_position = \
                self.screen_width // 2, self.screen_height // 2, 400, 320
        self.help_text_color = colors.BROWN
        self.help_back_color = colors.LIGHTSTEELBLUE
        self.help_text_size = 25
        self.help_font = "courier"
        self.help_text = \
            "       Game Controls       " + \
            "      ===============      " + \
            "F1         Help            " + \
            "S          Start           " + \
            "Left /                     " + \
            "Right      Ship Movement   " + \
            "Space      Ship Fire       " + \
            "P          Pause           " + \
            "C          Continue        " + \
            "Q          Quit          "

        self.slides_directory = "assets/images/slides/"
        self.slides_directory = Path(images_path, "slides")
        self.slide_delay = 1.5
