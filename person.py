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

    def description(self):
        return f"{self.first} {self.last} is {str(self.age)} years old. Their hair is {self.hair_color} and their eyes are {self.eye_color}."

    def birthday(self):
        self.age = int(self.age) + 1
        return f"Happy Birthday! {self.first} {self.last} is now {self.age}!"
