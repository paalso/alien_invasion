import random


WHITE = 255, 255, 255
BLACK = 0, 0, 0
RED = 255, 0, 0
GREEN = 0, 255, 0
BLUE = 0, 0, 255


def generate_random_color_level(max_level=255):
    return random.randint(0, max_level)


def generate_random_rgb_color(max_level=255):
    return (
            generate_random_color_level(max_level),
            generate_random_color_level(max_level),
            generate_random_color_level(max_level),
    )


def random_change_color_level(color_level, step):
    new_color_level = abs(color_level + random.randint(-step, step))
    if new_color_level > 255:
        excess = new_color_level - 255
        new_color_level = 256 - excess
    return new_color_level


