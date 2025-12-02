from Modulos.items.library_item import LibraryItem

class Magazine(LibraryItem):
    def __init__(self, title, author, price, edition):
        super().__init__(title, author, price)
        self.edition = edition

    def apply_dicount(self):
        self._price  -= (self._price * 0.05) # 5% discount