"""
Rectangle Module
~~~~~~~~~~~~~~~~

This module implements a Rectangle class that inherits from the BaseGeometry class.
It provides functionality to create and manipulate rectangles based on their width and height.

Classes:
    Rectangle: A class representing a rectangle with width and height.

"""

from typing import Any
BaseGeometry = __import__("7-base_geometry").BaseGeometry

class Rectangle(BaseGeometry):
    """
    A class representing a rectangle with width and height.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.
        
    Methods:
        __init__(width: int, height: int):
            Initializes a new Rectangle instance with the specified width and height.

    """

    def __init__(self, width: int, height: int) -> None:
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
