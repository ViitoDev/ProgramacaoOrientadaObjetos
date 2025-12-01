class Library:
    libraries = []

    def __init__(self, name):
        self.name = name
        self.active = False
        Library.libraries.append(self)

    def __str__(self):
        return self.name
    
    def listLibraries():
        for library in Library.libraries:
            print(f"{library.name} | {library.active}")
    
city_library = Library("City Library")
shopping_library = Library("Shopping Library")

Library.listLibraries()