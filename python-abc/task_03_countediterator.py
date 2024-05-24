#!/usr/bin/python3

class CountedIterator:

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.__count = 0

    def get_count(self):
        return self.__count
    
    def __iter__(self):
        return self
    
    def __next__(self):
        self.__count += 1
        item = next(self.iterator)
        return item
        
        

        
    
