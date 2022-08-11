import re
from turtle import width


class Rectangle:
    def __init__(self, width, height) -> None:
        self.width = width
        self.height = height
    
    def set_width(self, new_width):  # user inputs a new height value
        self.width = new_width

    def set_height(self,new_height): #user inputs a new height value
        self.height = new_height

    def get_area(self):
        return self.width*self.height
    
    def get_perimeter(self):
        return 2*(self.width+self.height)
    
    def get_diagonal(self):
        return ((self.width**2 + self.height**2) ** 0.5)

    def get_picture(self):
        point="*"
        if self.width < 50 and self.height < 50:
            return ("*" * self.width + "\n") * self.height
        else:
            return "Too big for picture."
    
    def get_amount_inside(self,shape):
        max_width = self.width // shape.width
        max_height = self.height // shape.height
        return max_width * max_height


    def __repr__(self): #This is the string representation of the object.
        return f"Rectangle(width={self.width}, height={self.height})"


class Square(Rectangle):
    def __init__(self, side):
        self.width=side
        self.height=side

    def __repr__(self):  # This is the string representation of the object.
        return f"Square(side={self.width})"

    def set_side(self, side):
        self.width = side
        self.height = side

    def set_width(self, side):
        self.width = side
        self.height = side

    def set_height(self, side):
        self.width = side
        self.height = side
