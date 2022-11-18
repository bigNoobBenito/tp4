from math import pi


class StringFoo:
    """

    """
    def __init__(self):
        """

        """
        self.message = ""

    def set_string(self, string: str):
        """

        :param string:
        :return:
        """
        self.message = string

    def __str__(self):
        """

        :return:
        """
        return self.message


class Rectangle:
    """

    """
    def __init__(self, width: int, height: int):
        """

        :param width:
        :param height:
        """
        self.width = width
        self.height = height

    def __str__(self):
        """

        :return:
        """
        return f"Rectangle: width={self.width}, height={self.height}"


class Circle:
    """

    """
    def __init__(self, radius: int):
        """

        :param radius:
        """
        self.radius = radius

    def __str__(self):
        """

        :return:
        """
        return f"Circle: radius={self.radius}"

    def area(self):
        """

        :return:
        """
        return pi * self.radius ** 2

    def circumference(self):
        """

        :return:
        """
        return 2 * pi * self.radius


class Hero:
    """

    """
    def __init__(self, name: str, level, strength: int, life: int, defense: int):
        """

        :param name:
        :param level:
        """
        self.name = name
        self.level = level
        self.strength = strength
        self.life = life
        self.defense = defense
print("Hello World")