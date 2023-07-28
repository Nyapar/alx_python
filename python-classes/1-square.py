#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size


try:
    square1 = Square(5)
    print(square1.__size)

    square2 = Square()     
    print(square2.__size)  

    square3 = Square("hello")  
    square4 = Square(-3)
except TypeError as e:
    print("TypeError:", e)
except ValueError as e:
    print("ValueError:", e)

