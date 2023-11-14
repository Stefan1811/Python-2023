class LibraryItem:
    def __init__(self,title,author,year):
        self.title=title
        self.author=author
        self.year=year
        self.check_out=False
    
    def library_checked_out(self):
        self.check_out=True
    
    def library_returned(self):
        self.check_out=False
    
    def library_details(self):
        pass

class Book(LibraryItem):
    def library_details(self):
        return f"{self.title} is a book that was written by {self.author} in {self.year} "

class DVD(LibraryItem):
    def library_details(self):
        return f"{self.title} is a DVD that was directed by {self.author} in {self.year} "

class   Magazine(LibraryItem):
    def library_details(self):
        return f"{self.title} is a magazine that was written by {self.author} in {self.year} "
    

book_instance = Book(title="The Great Gatsby", author="F. Scott Fitzgerald", year=1925)
dvd_instance = DVD(title="Inception", author="Christopher Nolan", year=2010)
magazine_instance = Magazine(title="National Geographic", author="Various", year=2022)

book_instance.library_checked_out()
dvd_instance.library_checked_out()

print(book_instance.library_details())
print(dvd_instance.library_details())
print(magazine_instance.library_details())

book_instance.library_returned()
dvd_instance.library_returned()
