class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
if __name__ == "__main__":

    book = Book("Harry Potter and the Sorcerer's Stone", "J. K. Rowling", 375)

print(f"The book name is '{book.title}', made by '{book.author}' and has {str(book.pages)} pages.")