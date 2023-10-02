#!/usr/bin/python3
"""presenter a class"""


class Rectangle:
    """introduce rectangle"""

    number_of_instances = 0
    print_symbol = '#'
    # public class attribute

    def __init__(self, width=0, height=0):
        """
            Intailize a new rectangle
            Args:
                width(int): width of new rectangle
                height(int): height of new rectangle
        """
        if (not isinstance(width, int)):
            raise TypeError('width must be an integer')
        if (width < 0):
            raise ValueError('width must be >= 0')
        if (not isinstance(height, int)):
            raise TypeError('height must be an integer')
        if (height < 0):
            raise ValueError('height must be >= 0')
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    def area(self):
        '''
        returns area rectangle instance
        '''
        return (self.__width * self.__height)

    def perimeter(self):
        '''
         return perimeter rectangle instance
        '''
        if ((self.__width == 0) or (self.__height == 0)):
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        if (self.__width == 0 or self.__height == 0):
            return ('')
        for i in range(0, self.__height):
            for j in range(0, self.__width):
                print(self.print_symbol, end='')
            if (self.__height - 1 != i):
                print('')
        return ('')

    def __repr__(self):
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        if (not isinstance(rect_1, Rectangle)):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if (not isinstance(rect_2, Rectangle)):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if (rect_1.area() < rect_2.area()):
            return (rect_2)
        else:
            return (rect_1)
