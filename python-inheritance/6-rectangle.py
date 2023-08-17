#!/usr/bin/python3
"""
This module implements a Rectangle object that inherits from BaseGeometry class.

Classes:
    Rectangle: Represents a rectangle with width and height.

"""

BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(width, height):
            Initializes a new Rectangle instance with the specified width and height.

    """

    def __init__(self, width, height):
        """
        Initialize a Rectangle instance with the specified width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            ValueError: If either width or height is not a positive integer.

        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
