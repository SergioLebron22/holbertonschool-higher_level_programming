#!/usr/bin/env python3

from abc import ABC, abstractmethod
from typing import Iterable, SupportsIndex

class VerboseList(list):

    def append(self, object: any) -> None:
        print(f"Added [{object}] to the list")
        return super().append(object)
    
    def extend(self, iterable: Iterable) -> None:
        print(f"Extended the list with [{len(iterable)}] items.")
        return super().extend(iterable)
    
    def remove(self, value: any) -> None:
        print(f"Removed [{value}] from the list.")
        return super().remove(value)
    
    def pop(self, index: SupportsIndex = -1) -> any:
        print(f"Popped [{self[index]}] from the list.")
        return super().pop(index)