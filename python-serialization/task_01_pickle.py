#!/usr/bin/python3


import pickle


class CustomObject:

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print(f"Name: {self.name}\nAge: \
{self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        try:
            pickle.dump(self, open(filename, "wb"))
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except (FileNotFoundError, IOError):
            return None
