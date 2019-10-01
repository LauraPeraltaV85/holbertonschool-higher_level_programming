#!/usr/bin/python3
class Square:
    """defines a square area, uses property and
       setter to set variables and prints square
       of hashtags"""

    def __init__(self, size=0, position=(0, 0)):
        self.__size = size
        self.__position = position

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        if:
            raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        return self.__size * self.__size

    def my_print(self):
        if self.size == 0:
            print()
        else:
            for count in range(self.size):
                for count in range(self.size):
                    print('#', end='')
                print()
