from abc import ABC, abstractmethod

class LibraryItem():
    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        self._price = price
    
    @abstractmethod
    def apply_dicount(self):
        pass 