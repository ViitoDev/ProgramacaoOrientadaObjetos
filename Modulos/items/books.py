from Modulos.items.library_item import LibraryItem

class Book(LibraryItem):
    def __init__(self, title, author, price, isbn):
        super().__init__(title, author, price)
        self.isbn = isbn

    def apply_dicount(self):
        self._price -= (self._price * 0.10) # 10% discount