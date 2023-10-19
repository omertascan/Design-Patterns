# Flyweight (Hafif) sınıfı
class Color:
    def __init__(self, name):
        self.name = name

# Flyweight Factory (Hafif Nesne Fabrikası)
class ColorFactory:
    colors = {}

    @staticmethod
    def get_color(name):
        if name not in ColorFactory.colors:
            ColorFactory.colors[name] = Color(name)
        return ColorFactory.colors[name]

if __name__ == "__main__":
    rainbow = ["Red", "Orange", "Yellow", "Green", "Blue", "Indigo", "Violet"]
    color_objects = []

    for color in rainbow:
        color_obj = ColorFactory.get_color(color)
        color_objects.append(color_obj)

    for color_obj in color_objects:
        print(f"Color: {color_obj.name}")


