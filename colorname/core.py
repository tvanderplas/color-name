
from PIL import ImageGrab
import colorsys

def get_color_name(r, g, b):
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    h *= 360
    if r < 15 and g < 15 and b < 15:
        return "black"
    elif r > 220 and g > 220 and b > 220:
        return "white"
    elif h < 30 or h >= 330:
        return "red"
    elif 30 <= h < 90:
        return "yellow"
    elif 90 <= h < 150:
        return "green"
    elif 150 <= h < 210:
        return "cyan"
    elif 210 <= h < 270:
        return "blue"
    elif 270 <= h < 330:
        return "magenta"
    else:
        return "unknown"

def get_pixel_color(x, y):
    '''Returns RGB data from the given pixel coordinates'''
    return ImageGrab.grab(bbox=(x, y, x + 1, y + 1)).getdata()[0]

def get_pixel_color_name(x, y):
    '''Returns the name of a color at the given pixel coordinates'''
    color = get_pixel_color(x, y)
    return get_color_name(*color)
