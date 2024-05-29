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
        pickle.dump(self, open(filename, "wb"))

    @classmethod
    def deserialize(cls, filename):
        cls = pickle.load(open(filename, "rb"))
        return cls
