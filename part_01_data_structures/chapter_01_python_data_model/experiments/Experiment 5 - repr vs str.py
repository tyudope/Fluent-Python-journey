class Book:

    def __init__(self, title:str, author:str):
        self.title = title
        self.author = author


    def __repr__(self):
        return f"Book {self.title} , {self.author}"

    def __str__(self):
        return f"Book Title : {self.title}\nBook Author: {self.author}"



book = Book(title = "Lord of the Rings: Return of the king" , author = "J.R.R Tolkien")
print(book)
print([book])

# Rule :
# __repr__ is for developers.
# __str__ is for users.

