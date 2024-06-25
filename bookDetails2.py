class Book:

    def __init__(self, title, author, pages):
        self.titulo = title
        self.author = author
        self.pages = pages

    #Metódo que deriva da classe object e é chamado quando fazemos print do objecto
    def __str__(self):
        return f"O livro {self.title} foi escrito por {self.author} e tem {self.pages} páginas."


l1 = Book("Python", "Guido van Rossum", 159)
l2 = Book("Java", "James Gosling", 200)

print(l1)
print(l2)