class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f" Pages: {self.pages}")
    
class LibraryBook(Book):
    def __init__(self, title, author, pages):
        super(). __init__(title, author, pages)
        self.is_available  = True
    
    def borrow_book(self):
        if self.is_available:
            self.is_available = False
            print("Book borrowed")
        else:
            print("Book is unavailable")
    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print("Book returned")
        else:
            print("Book was not borrowed")

Book1 = LibraryBook("Kusuma The Programmer", "Rusthum", 150)
Book1.display()
Book1.borrow_book()
Book1.return_book()


       