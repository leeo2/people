# Olivia Lee
# 11-13-19
# Person class

class Person():

    def __init__(self, first, last, age, hair_color, eye_color):
        self.first = first
        self.last = last
        self.age = age
        self.hair_color = hair_color
        self.eye_color = eye_color

    def description(self, first, last, age, hair_color, eye_color):
        return f"{first} {last} is " + str(self.age) + f"years old. Their hair is {self.hair_color} and their eyes {self.eye_color}."

    def birthday(self, age):
        self.age = self.age + 1
