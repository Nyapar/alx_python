"""
based on 0-square.py
"""

class Square:
    """
    task 1 classes
    """
    def __init__(self, size):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not init:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

        def area(self):
            return self.size ** 2

        def my_print(self):
            if self.__size == 0:
                print(0)
            else:
                for row in range(self.__size):
                    for column in range(kself.__size):
                        print("#", end ="")
