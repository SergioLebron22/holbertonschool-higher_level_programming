#!/usr/bin/python3

class SwimMixin:

    def swim(self):
        print("The creature swims!")

class FlyMixin:

    def fly(self):
        print("This crature flies!")

class Dragon(SwimMixin, FlyMixin):

    def roar(self):
        print("This dragon roars!")