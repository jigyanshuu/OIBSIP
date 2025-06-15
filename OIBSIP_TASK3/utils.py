import os

def get_weather_icon(condition_name, animated=False):
    """
    Returns the path to the weather icon (static or animated) based on the condition.
    Looks into 'assets/animated_weather_icons' or 'assets/icons'.
    """
    condition_name = condition_name.lower()

    icon_map = {
        "clear": "clear",
        "clouds": "clouds",
        "rain": "rain",
        "snow": "snow",
        "thunderstorm": "thunderstorm",
        "mist": "mist",
        "fog": "fog",
        "haze": "haze",
        "drizzle": "drizzle",
    }

    folder = "assets/animated_weather_icons" if animated else "assets/icons"
    filename = icon_map.get(condition_name, "default")
    extension = ".gif" if animated else ".png"
    icon_path = os.path.join(folder, filename + extension)

    if os.path.exists(icon_path):
        return icon_path
    else:
        # fallback to default icon if not found
        return os.path.join(folder, "default" + extension)
